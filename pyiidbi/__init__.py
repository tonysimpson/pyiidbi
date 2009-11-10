from errors import *
import base

class Cursor(object):
    def cursor_method(close_open_statement):
        """Most cursor methods need to aquire the connection lock etc. This
        decorator performs the start and end tasks required by most cursor
        methods.

        """
        def decorator(func):
            def wrapper(self, *args, **kwargs):
                if self.__closed:
                    Error('Cursor is closed')
                try:
                    self.__conn.lock.acquire() # aquire the connection lock
                    if self.__open_stmt and close_open_statement: #should close previous stmt
                        try:
                            base.close_or_cancel_open_statement(self.__open_stmt)
                        finally:
                            self.__open_stmt = None

                    return func(self, *args, **kwargs) # execute wrapped function
                finally:
                    self.__conn.lock.release() # release the connection lock
            wrapper.__name__ = func.__name__
            wrapper.__doc__  = func.__doc__
            return wrapper
        return decorator

    def __init__(self, conn):
        self.__conn      = conn
        self.__open_stmt = None
        self.description = property(fget = self.__get_description)
        self.rowcount    = property(fget = self.__get_rowcount)
        self.__rowcount  = -1
        self.arraysize   = 1
        self.__closed    = False

    def __get_rowcount(self):
        if self.__open_stmt:
            return self.__open_stmt.rowcount
        else:
            return self.__rowcount

    def __get_description(self):
        if self.__open_stmt:
            return self.__open_stmt.description
        else:
            return None

    @cursor_method(close_open_statement=True)
    def close(self):
        self.__rowcount    = -1
        self.__closed    = True

    @cursor_method(close_open_statement=True)
    def execute(self, operation, parameters=None):
        """Execute a statement or command.

        """
        query_type, can_prepare, row_returning, error_msg = base.identify_query(operation)
        if error_msg: # there are issues with this type of query
            raise ProgrammingError(error_msg)

        if row_returning:
            self.__open_stmt = base.cursor(self.__conn, operation, parameters)
        else:
            self.__rowcount = base.query(self.__conn, operation, parameters)

    @cursor_method(close_open_statement=True)
    def execute_many(self, operation, seq_of_parameters):
        """Execute a statement or command once for each set fo parameters.

           The statement will be prepaired if possible.
           Row producing statements are not supported, use multiple calls to
           'execute' instead.

        """
        query_type, can_prepare, row_returning, error_msg = identify_query(operation)
        if error_msg: # there are issues with this type of query
            raise ProgrammingError(error_msg)
        if row_returning: # fetch is not supported
            raise ProgrammingError("Row producing statements are not " +
                         "supported, use multiple calls to 'execute' instead.")
        if can_prepare:
            # TODO: need to track prepared queries when autocommit is on
            #       as they may not get cleaned up
            prepared_id = prepare(self.__conn, operation)
            for parameters in seq_of_parameters:
                execute(self.__conn, prepared_id, parameters)
        else:
            for parameters in seq_of_parameters:
                query(self.__conn, operation, parameters)

    @cursor_method(close_open_statement=True)
    def callproc(self, procname, parameters=None):
        """Execute stored procedure.

        Return: Modified parameters.

        """
        self.__open_stmt = executeproc(self.__conn, procname, parameters)

    @cursor_method(close_open_statement=False)
    def fetchall(self):
        try:
            return base.fetchall(self.__conn, self.__open_stmt)
        finally:
            self.__open_stmt = None

    @cursor_method(close_open_statement=False)
    def fetchmany(self, size=None):
        if size == None:
            size = self.arraysize
        pass

    @cursor_method(close_open_statement=False)
    def fetchone(self):
        pass

    def __del__(self):
        self.close()




class Connection(object):
    def connection_method(func):
        """Most connection methods need to aquire the connection lock etc. This
        decorator performs the start and end tasks required by most connection
        methods.

        """
        def wrapper(self, *args, **kwargs):
            if self.__closed:
                Error('Connection is closed')
            try:
                self.__conn.lock.acquire() # aquire the connection lock
                return func(self, *args, **kwargs) # execute wrapped function
            finally:
                self.__conn.lock.release() # release the connection lock
        wrapper.__name__ = func.__name__
        wrapper.__doc__  = func.__doc__
        return wrapper

    def __init__(self,conn):
        self.__conn   = conn
        self.__closed = False

    @connection_method
    def rollback(self):
        base.rollback(self.__conn)

    @connection_method
    def commit(self):
        base.commit(self.__conn)

    @connection_method
    def close(self):
        try:
            base.disconnect(self.__conn)
        finally:
            self.__closed == true

    def cursor(self):
        cur = Cursor(self.__conn)
        return cur

    def __del__(self):
        self.close()

def connect(database, username=None, password=None, environment=None):
    """Creates a database connection.

    """
    return Connection(base.connect(database, username, password, environment))

__ALL__ = ['connect', 'Error', 'Warning']
