from iiapi import *
from ctypes import *
from exceptions import StandardError
from warnings import warn

warning = warn
message = warn

def wait(gen_parm):
    """Call IIapi_wait until gp_completed.

    """
    wait_parm = IIAPI_WAITPARM()
    wait_parm.wt_timeout = -1
    while not gen_parm.gp_completed:
        IIapi_wait(byref(wait_parm))

def raise_errors(gen_parm):
    """Raise internal exceptions to be handled by interface layer.

    """
    if gen_parm.gp_status != IIAPI_ST_SUCCESS:
        if gen_parm.gp_status == IIAPI_ST_NO_DATA:
            raise StopIteration()
        if not gen_parm.gp_errorHandle:
            raise DatabaseError(''.join([attr for attr in dir() if attr.startswith('IIAPI_ST_')
                           and globals()[attr] == gen_parm.gp_status]) or 'Unknown error')
        geteinfo_parm = IIAPI_GETEINFOPARM()
        geteinfo_parm.ge_errorHandle = gen_parm.gp_errorHandle
        while 1:
            IIapi_getErrorInfo(byref(geteinfo_parm))
            if geteinfo_parm.ge_status == IIAPI_ST_NOT_INITIALIZED:
               raise DatebaseError('Error handler not initialized')
            elif geteinfo_parm.ge_status == IIAPI_ST_INVALID_HANDLE:
               raise DatebaseError('Error handler invalid')
            if geteinfo_parm.ge_type == IIAPI_GE_ERROR:
                raise IngresError(geteinfo_parm.ge_message, geteinfo_parm.ge_SQLSTATE,
                                                            geteinfo_parm.ge_errorCode)
            elif geteinfo_parm.ge_type == IIAPI_GE_WARNING:
                raise IngresWarning(geteinfo_parm.ge_message, geteinfo_parm.ge_SQLSTATE,
                                                            geteinfo_parm.ge_errorCode)
            elif geteinfo_parm.ge_type == IIAPI_GE_MESSAGE:
                message(geteinfo_parm.ge_message)

            if geteinfo_parm.ge_status == IIAPI_ST_NO_DATA: #done
                break

def wait_and_raise_errors(gen_parm):
    """Call wait then raise_errors

    """
    wait(gen_parm)
    raise_errors(gen_parm)

class Error(StandardError):
    pass

class Warning(StandardError):
    pass

class InterfaceError(Error):
    pass

class DatabaseError(Error):
    pass

class InternalError(DatabaseError):
    pass

class OperationalError(DatabaseError):
    pass

class ProgrammingError(DatabaseError):
    pass

class IntegrityError(DatabaseError):
    pass

class DataError(DatabaseError):
    pass

class NotSupportedError(DatabaseError):
    pass

class IngresError(DatabaseError):
    """Ingres Error

    """
    def __init__(self, msg, sql_state, error_code):
        DatabaseError.__init__(self, str(msg))
        self.msg = msg
        self.sql_state  = sql_state
        self.error_code = int(error_code)

    def __str__(self):
        return "%d %s [%s]" % (self.error_code, self.sql_state, self.msg)

    def __repr__(self):
        return str(self)

class IngresWarning(IngresError):
    pass
