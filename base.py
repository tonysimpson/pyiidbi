from iiapi import *
from ctypes import *
from struct import pack, unpack
from errors import *
from datetime import datetime, timedelta, date, time

ENV_HANDLE = None

def init():
    global ENV_HANDLE
    init_parm = IIAPI_INITPARM()
    init_parm.in_timeout = -1
    init_parm.in_version = IIAPI_VERSION_6
    IIapi_initialize(byref(init_parm))
    if init_parm.in_status != IIAPI_ST_SUCCESS:
        raise Exception('Could not initialize OpenAPI.')
    ENV_HANDLE = init_parm.in_envHandle
    setenvprm_parm = IIAPI_SETENVPRMPARM()
    setenvprm_parm.se_envHandle = ENV_HANDLE;
    setenvprm_parm.se_paramID = IIAPI_EP_MAX_SEGMENT_LEN;
    setenvprm_parm.se_paramValue = cast(pointer(c_long(SEG_LENGTH)), c_void_p)
    IIapi_setEnvParam(byref(setenvprm_parm));
    if setenvprm_parm.se_status != IIAPI_ST_SUCCESS:
        raise Exception('Failed to set segment length.')

__init__()

def __del__():
    term_parm = IIAPI_TERMPARM()
    IIapi_terminate(byref(term_parm))
    if term_parm.tm_status == IIAPI_ST_SUCCESS:
        global ENV_HANDLE
        del ENV_HANDLE
    else:
        if term_parm.tm_status == IIAPI_ST_NOT_INITIALIZED:
            raise Exception('OpenAPI was never initialized')
        elif term_parm.tm_status == IIAPI_ST_WARNING:
            warning('OpenAPI has been initialized more than once')

class ConnectionState(object):
    """Stores connection information and state.

    """
    def __init__(self):
        self.conn_handle = None
        self.tran_handle = None
        self.stmt_handle = None #active statement
        self.data_buffer = None #buffer mem location
        self.data_buflen = None #buffer length
        self.dv_array    = None
        self.lock        = threading.RLock()

def close_or_cancel_open_statement(self):
    if self.stmt_handle:
        if self.active_query:
            cancel_parm = IIAPI_CANCELPARM()
            cancel_parm.cn_stmtHandle = self.stmt_handle
            IIapi_cancel(byref(cancel_parm))
            try:
                wait_and_raise_errors(cancel_parm.cn_genParm)
            except:
                pass
            finally:
                self.active_query = False
        close_parm = IIAPI_CLOSEPARM()
        close_parm.cl_stmtHandle = self.stmt_handle
        IIapi_close(byref(close_parm))
        try:
            wait_and_raise_errors(close_parm.cl_genParm)
        finally:
            self.stmt_handle = None
            self.row_count   = -1
            self.description = None




    def __iter__(self):
        def row_iterator():
            for row in results_gen(self.stmt_handle, self.description, self.buffer, self.buffer_byte_len):
                yield row

            getqinfo_parm = IIAPI_GETQINFOPARM()
            getqinfo_parm.gq_stmtHandle = self.stmt_handle
            IIapi_getQueryInfo(byref(getqinfo_parm))
            wait_and_raise_errors(getqinfo_parm.gq_genParm)
            if getqinfo_parm.gq_mask & IIAPI_GQ_ROW_COUNT:
                self.row_count = getqinfo_parm.gq_rowCount

            close_parm = IIAPI_CLOSEPARM()
            close_parm.cl_stmtHandle = self.stmt_handle
            IIapi_close(byref(close_parm))
            try:
                wait_and_raise_errors(close_parm.cl_genParm)
            finally:
                self.stmt_handle = None
                self.active_query = False

        return row_iterator()

def identify_query(query):
    for regexp, query_type, can_prepare, returns_rows, error_msg in SQL_QUERY_TYPES:
        if regexp.match(query):
            return quert_type, can_prepare, returns_rows, error_msg
    return IIAPI_QT_QUERY, False, False, None

SQL_QUERY_TYPES = ]
    (re.compile(r"(?i)\s*SELECT"), IIAPI_QT_OPEN, True, True, None),
    (re.compile(r"(?i)\s*(?:INSERT|UPDATE|DELETE)"), IIAPI_QT_QUERY, True, False, None),
    (re.compile(r"(?i)\s*(?:CREATE|ALTER|DROP|GRANT|REVOKE|MODIFY|SET)"), IIAPI_QT_QUERY, False, False, None),
    (re.compile(r"(?i)\s*COMMIT"), None, None, None, "Use Connection 'commit' method to COMMIT."),
    (re.compile(r"(?i)\s*ROLLBACK"), None, None, None, "Use Connection 'rollback' method to ROLLBACK."),
    (re.compile(r"(?i)\s*(?:OPEN|CLOSE)"), None, None, None, "Cursor statements not supported."),
    (re.compile(r"(?i)\s*SET\s+AUTOCOMMIT"), None, None, None, "Use Connection 'autocommit' method to set autocommit."),
    (re.compile(r"(?i)\s*(?:CALL|EXECUTE\s+PROCEDURE)"), None, None, None, "Use Cursor 'callproc' method to call procedures."),
    (re.compile(r"(?i)\s*COPY"), None, None, None, "COPY statement not supported.")
]

MAX_CHAR = 32*1024
SEG_LENGTH  = 4*1024

def display_length(data_type, length):
    return None
def get_description(stmt_handle):
    getdescr_parm = IIAPI_GETDESCRPARM()
    getdescr_parm.gd_stmtHandle = stmt_handle
    IIapi_getDescriptor(byref(getdescr_parm))
    wait_and_raise_errors(getdescr_parm.gd_genParm)
    if not getdescr_parm.gd_descriptorCount:
        return None
    else:
        descriptors = getdescr_parm.gd_descriptor
        res = [None]*getdescr_parm.gd_descriptorCount
        for i in range(getdescr_parm.gd_descriptorCount):
            desc = descriptors[i]
            res[i] = (desc.ds_columnName,
                  desc.ds_dataType,
                  display_length(desc.ds_dataType,desc.ds_length),
                  desc.ds_length,
                  desc.ds_precision,
                  desc.ds_scale,
                  desc.ds_nullable == 1)
        return res


# Set and send parameters
class Parameter(object):
    """Parameter information structure

    """

    __slots__ = ['value', 'is_long', 'nullable', 'data_value', 'scale',
                 'precision', 'data_type', 'col_type', 'col_name']

    is_long    = False
    nullable   = False
    scale      = 0
    precision  = 0

    def __init__(self, value, col_type, col_name=None):
        self.value    = value
        self.col_type = col_type
        self.col_name = col_name

        if value == None:
            self.data_type = IIAPI_LTXT_TYPE
            data_value = lambda : (True, 0, None)
            self.nullable  = True
            self.length    = 0
            #data_value defaults to null data value
        elif type(value) == str:
            self.__init_buffer_type(value, IIAPI_VCH_TYPE, IIAPI_LVCH_TYPE)
        elif isinstance(value, unicode):
            self.__init_wbuffer_type(value, IIAPI_VCH_TYPE, IIAPI_LVCH_TYPE)
        elif isinstance(value, int) or isinstance(value, long):
            self.data_type  = IIAPI_INT_TYPE
            self.length     = 8
            self.data_value = lambda : (False, self.length, pack('l', value))
        elif isinstance(value, float):
            self.data_type  = IIAPI_FLT_TYPE
            self.length     = 8
            self.data_value = lambda : (False, self.length, pack('d', value))
        elif isinstance(value, chars):
            self.data_type  = IIAPI_CHA_TYPE
            self.length     = len(value)
            self.data_value = lambda : (False, self.length, value)
        elif (isinstance(value, date) or isinstance(value, time) or
                isinstance(value, datetime) or isinstance(value, timedelta)):
            if isinstance(value, date):
                value = value.strftime('%Y_%m_%d')
            elif isinstance(value, time):
                value = value.strftime('%H:%M:%S')
            elif isinstance(value, datetime):
                value = value.strftime('%Y_%m_%d %H:%M:%S')
            elif isinstance(value, timedelta):
                value = '%d days %d seconds' % (value.days, value.seconds)
            self.data_type  = IIAPI_CHA_TYPE
            self.length     = len(value)
            self.data_value = lambda : (False, self.length, value)
        elif isinstance(value, bytes):
            self.__init_buffer_type(value, IIAPI_VBYTE_TYPE, IIAPI_LBYTE_TYPE)
        elif isinstance(value, str):
            self.__init_buffer_type(value, IIAPI_VCH_TYPE, IIAPI_LVCH_TYPE)
        elif hasattr(value, 'read'):
            self.__init_stream_type(value)
        else:
            raise InterfaceError('Unhandled type %s as parameter' % type(value))

    def __seg_gen(self, value):
        if not value:
            yield pack('H',0)
        else:
            for i in xrange(0, len(value), SEG_LENGTH):
                segment = value[i:i+SEG_LENGTH]
                yield pack('H', len(segment)) + segment

    def __wseg_gen(self, value):
        if not value:
            yield pack('H',0)
        else:
            for i in xrange(0, len(value), SEG_LENGTH//2):
                segment = value[i:i+SEG_LENGTH//2].encode('utf-16') # utf-16 != ucs2 but I don't care!
                yield pack('H', len(segment)//2) + segment

    def __stream_seg_gen(self, value):
        while True:
            segment = value.read(SEG_LENGTH)
            if segment:
                yield pack('H', len(segment)) + segment
                if len(segment) != SEG_LENGTH:
                    break
            else:
                yield pack('H',0)

    def __init_buffer_type(self, value, type, long_type):
        if len(value) > MAX_CHAR :
            self.data_type  = long_type
            self.length     = SEG_LENGTH
            self.is_long    = True
            self.data_value = lambda : ((False, len(segment), segment)
                                        for segment in self.__seg_gen(value))
        else:
            self.data_type = type
            self.length    = len(value)
            self.data_value = lambda : (False, self.length+2,
                                                pack('H',self.length) + value)

    def __init_wbuffer_type(self, value, type, long_type):
        if len(value) > (MAX_CHAR //2):
            self.data_type = long_type
            self.length    = SEG_LENGTH
            self.is_long   = True
            self.data_value = lambda : ((False, len(segment), segment)
                                        for segment in self.__wseg_gen(value))
        else:
            self.data_type = type
            self.length    = len(value)
            value = value.encode('utf-16')
            self.data_value = lambda : (False, len(value)+2,
                                pack('H', self.length) + value)

    def __init_stream_type(self, value):
        self.data_type = IIAPI_LBYTE_TYPE
        self.length    = SEG_LENGTH
        self.is_long   = True
        self.data_value = lambda : ((False, len(segment), segment)
                                     for segment in self.__stream_seg_gen(value))


def set_description(conn, params):
    """Set the parameter description for the statement.

    Comes after statement creation and before sending parameters.

    params: sequence of Parameter objects.

    """
    desc_array  = (IIAPI_DESCRIPTOR * len(params))()
    for i in range(len(params)):
        desc = desc_array[i]
        param = params[i]
        desc.ds_dataType   = param.data_type
        desc.ds_nullable   = param.nullable
        desc.ds_length     = param.length
        desc.ds_precision  = param.precision
        desc.ds_scale      = param.scale
        desc.ds_columnType = param.col_type
        desc.ds_columnName = param.col_name
    setdescr_parm                    = IIAPI_SETDESCRPARM()
    setdescr_parm.sd_stmtHandle      = stmt_handle
    setdescr_parm.sd_descriptorCount = len(params)
    setdescr_parm.sd_descriptor      = desc_array
    IIapi_setDescriptor(byref(setdescr_parm))
    #TODO: fix this
    wait_and_raise_errors(setdescr_parm.sd_genParm)


def send_params(conn, params)
    putparm_parm                 = IIAPI_PUTPARMPARM()
    putparm_parm.pp_stmtHandle   = conn.stmt_handle
    putparm_parm.pp_parmData     = conn.dv_array

    data_offset = conn.data_buffer
    j = 0
    for i in range(len(params)):
        if params[i].is_long:
            if j: # send prev params
                putparm_parm.pp_parmCount = j
                putparm_parm.pp_moreSegments = False
                IIapi_putParms(byref(putparm_parm))
                wait_and_raise_errors(putparm_parm.pp_genParm)
            dv_gen = params[i].data_value()
            dv_null, dv_length, dv_value = dv_gen.next()
            while True:
                dv = putparm_parm.pp_parmData[0]
                dv.dv_null   = dv_null
                dv.dv_length = dv_length
                data_offset = conn.data_buffer
                memmove(data_offset, dv_value, dv_length)
                dv.dv_value  = data_offset
                try:
                    dv_null, dv_length, dv_value = dv_gen.next()
                    has_more = True
                except:
                    has_more = False
                putparm_parm.pp_parmCount = 1
                putparm_parm.pp_moreSegments = has_more
                IIapi_putParms(byref(putparm_parm))
                wait_and_raise_errors(putparm_parm.pp_genParm)
                if not has_more:
                    j = 0
                    data_offset = conn.data_buffer
                    break
        else:
            dv_null, dv_length, dv_value = params[i].data_value()
            dv = putparm_parm.pp_parmData[j]
            dv.dv_null   = dv_null
            dv.dv_length = dv_length
            memmove(data_offset, dv_value, dv_length)
            dv.dv_value  = data_offset
            data_offset += dv_length
            j += 1
    if j:
        putparm_parm.pp_parmCount = j
        putparm_parm.pp_moreSegments = False
        IIapi_putParms(byref(putparm_parm))
        wait_and_raise_errors(putparm_parm.pp_genParm)

def cursor(self, stmt, parameters=None):
    query_parm = IIAPI_QUERYPARM()
    query_parm.qy_connHandle = self.conn.conn_handle
    query_parm.qy_queryType  = IIAPI_QT_OPEN
    query_parm.qy_queryText  = stmt
    query_parm.qy_parameters = True
    query_parm.qy_tranHandle = self.conn.tran_handle
    IIapi_query(byref(query_parm))
    try:
        wait_and_raise_errors(query_parm.qy_genParm)
    finally:
        self.stmt_handle  = query_parm.qy_stmtHandle
        self.active_query = True
        if not self.conn.tran_handle:
            self.conn.tran_handle = query_parm.qy_tranHandle

    params = (Parameter(chars('pyiidbi_cur_'+self.id), IIAPI_COL_SVCPARM),)
    if parameters:
        params += tuple(Parameter(p, IIAPI_COL_QPARM) for p in parameters)

    set_description(self.stmt_handle, params)
    send_params(self.stmt_handle, params)
    self.description = get_description(self.stmt_handle)

def results_gen(stmt_handle, description, buffer, buffer_byte_len):
    if description:
        row_byte_len    = sum(desc[3] for desc in description)
        row_count       = buffer_byte_len // row_byte_len
        col_count       = len(description)

        if row_count > 50:
            row_count = 50
        elif row_count < 1:
            buffer_byte_len = row_byte_len
            buffer = cast(pointer(create_string_buffer(buffer_byte_len)), c_void_p)
            row_count = 1

        getcol_parm                = IIAPI_GETCOLPARM()
        getcol_parm.gc_stmtHandle  = stmt_handle
        getcol_parm.gc_rowCount    = row_count
        getcol_parm.gc_columnCount = col_count
        getcol_parm.gc_columnData  = (IIAPI_DATAVALUE*(col_count*row_count))()

        buffer_base = buffer.value
        byte_offset = 0

        col_data = getcol_parm.gc_columnData
        for i in range(row_count):
            for j in range(col_count):
                length = description[j][3]
                dv     = col_data[i*col_count+j]
                dv.dv_value   = c_void_p(buffer_base + byte_offset)
                byte_offset += length

        while 1:
            IIapi_getColumns(byref(getcol_parm))
            try:
                wait_and_raise_errors(getcol_parm.gc_genParm)
            except StopIteration:
                break
            col_data = getcol_parm.gc_columnData
            returned_row_count = getcol_parm.gc_rowsReturned

            for i in range(returned_row_count):
                res = [None]*(col_count)
                for j in range(col_count):
                    dv = col_data[i*col_count+j]
                    if not dv.dv_null:
                        res[j] = string_at(dv.dv_value, dv.dv_length)
                yield tuple(res)

class DBAPITypeObject:
    def __init__(self,*values):
        self.values = values
    def __cmp__(self,other):
        if other in self.values:
            return 0
        if other < self.values:
            return 1
        else:
            return -1

#types

class chars(str):
    """Represents an IIAPI_CHA_TYPE in Ingres"""
    pass

class bytes(str):
    """Represents Ingres BYTE types"""
    pass
"""
STRING
BINARY
NUMBER
DATETIME
ROWID
"""


def connect(database, username=None, password=None, environment=None):
    con_parm               = IIAPI_CONNPARM()
    con_parm.co_target     = database
    con_parm.co_username   = username
    con_parm.co_password   = password
    con_parm.co_timeout    = -1
    con_parm.co_connHandle = ENV_HANDLE
    con_parm.co_type       = IIAPI_CT_SQL
    IIapi_connect(byref(con_parm))
    try:
        wait_and_raise_errors(con_parm.co_genParm)
    except Exception, exc:
        if con_parm.co_connHandle:
            abort_parm = IIAPI_ABORTPARM()
            abort_parm.ab_connHandle = con_parm.co_connHandle
            IIapi_abort(byref(abort_parm))
        raise exc
    return Connection(con_parm.co_connHandle)

def disconnect(connection):
    if not self.conn_handle:
        return
    for cursor_wref in self.cursor_wrefs:
        if cursor_wref():
            cursor_wref().close()
    disconn_parm = IIAPI_DISCONNPARM()
    disconn_parm.dc_connHandle = self.conn_handle
    IIapi_disconnect(byref(disconn_parm))
    try:
        wait_and_raise_errors(disconn_parm.dc_genParm)
    except IngresError, exc:
        abort_parm = IIAPI_ABORTPARM()
        abort_parm.ab_connHandle = self.conn_handle
        IIapi_abort(byref(abort_parm))
        warning(str(exc))
    finally:
        self.conn_handle = None
