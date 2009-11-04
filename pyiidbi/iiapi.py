'''Wrapper for iiapi.h

Generated with:
ctypesgen.py -L/home/ingres/IngresII/ingres/lib -llibframe.1.so -llibq.1.so -llibiiapi.1.so -I/home/ingres/IngresII/ingres/files /home/ingres/IngresII/ingres/files/iiapi.h -o ../pyiidbi/pyiiapi.py

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x
        p.from_param = classmethod(from_param)

    return p

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return long(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxint):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxint):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxint):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxint):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxint):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxint):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxint):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, unicode, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0
    
    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)
        
        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj
        
        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj
        
        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))


# End preamble


_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions 
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright 
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]
    
    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)
        
        for path in paths:
            if os.path.exists(path):
                return self.load(path)
        
        raise ImportError("%s not found." % libname)
    
    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
        except OSError,e:
            raise ImportError(e)
    
    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        
        else:
            for path in self.getplatformpaths(libname):
                yield path
            
            path = ctypes.util.find_library(libname)
            if path: yield path
    
    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]
    
    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]
        
        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)
    
    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:
        
        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']
        
        dirs = []
        
        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")
        
        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)
        
        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None
    
    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        directories.extend(['/lib', '/usr/lib', '/lib64', '/usr/lib64'])

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path
                    
                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache
    
    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll"]
    
    def load(self, path):
        return _WindowsLibrary(path)
    
    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader,
    "win64":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

II_SYSTEM=os.getenv('II_SYSTEM')

if not II_SYSTEM:
    raise Exception('II_SYSTEM must be set')

add_library_search_dirs([os.path.join(II_SYSTEM,'/ingres/lib')])
add_library_search_dirs([os.path.join(II_SYSTEM,'/ingres/bin')])

# Begin libraries
if sys.platform in ('cygwin','win32', 'win64'):
    _libs["iilibapi.dll"] = load_library('iilibapi')
else:
    _libs["librt.so.1"] = load_library("librt.so.1")
    _libs["libframe.1.so"] = load_library("libframe.1.so")
    _libs["libq.1.so"] = load_library("libq.1.so")
    _libs["libiiapi.1.so"] = load_library("libiiapi.1.so")

# End libraries

# No modules

II_BOOL = c_int # /home/ingres/IngresII/ingres/files/iiapidep.h: 5

II_CHAR = c_char # /home/ingres/IngresII/ingres/files/iiapidep.h: 6

II_INT2 = c_short # /home/ingres/IngresII/ingres/files/iiapidep.h: 9

II_INT4 = c_int # /home/ingres/IngresII/ingres/files/iiapidep.h: 10

II_LONG = c_int # /home/ingres/IngresII/ingres/files/iiapidep.h: 12

II_PTR = c_void_p # /home/ingres/IngresII/ingres/files/iiapidep.h: 15

II_UINT2 = c_ushort # /home/ingres/IngresII/ingres/files/iiapidep.h: 18

II_UINT4 = c_uint # /home/ingres/IngresII/ingres/files/iiapidep.h: 19

II_UINT8 = c_ulonglong # /home/ingres/IngresII/ingres/files/iiapidep.h: 20

II_ULONG = c_uint # /home/ingres/IngresII/ingres/files/iiapidep.h: 21

IIAPI_DT_ID = II_INT2 # /home/ingres/IngresII/ingres/files/iiapi.h: 530

IIAPI_STATUS = II_ULONG # /home/ingres/IngresII/ingres/files/iiapi.h: 611

IIAPI_QUERYTYPE = II_ULONG # /home/ingres/IngresII/ingres/files/iiapi.h: 647

# /home/ingres/IngresII/ingres/files/iiapi.h: 734
class struct__IIAPI_DATAVALUE(Structure):
    pass

struct__IIAPI_DATAVALUE.__slots__ = [
    'dv_null',
    'dv_length',
    'dv_value',
]
struct__IIAPI_DATAVALUE._fields_ = [
    ('dv_null', II_BOOL),
    ('dv_length', II_UINT2),
    ('dv_value', II_PTR),
]

IIAPI_DATAVALUE = struct__IIAPI_DATAVALUE # /home/ingres/IngresII/ingres/files/iiapi.h: 734

# /home/ingres/IngresII/ingres/files/iiapi.h: 813
class struct__IIAPI_DESCRIPTOR(Structure):
    pass

struct__IIAPI_DESCRIPTOR.__slots__ = [
    'ds_dataType',
    'ds_nullable',
    'ds_length',
    'ds_precision',
    'ds_scale',
    'ds_columnType',
    'ds_columnName',
]
struct__IIAPI_DESCRIPTOR._fields_ = [
    ('ds_dataType', IIAPI_DT_ID),
    ('ds_nullable', II_BOOL),
    ('ds_length', II_UINT2),
    ('ds_precision', II_INT2),
    ('ds_scale', II_INT2),
    ('ds_columnType', II_INT2),
    ('ds_columnName', c_char_p),
]

IIAPI_DESCRIPTOR = struct__IIAPI_DESCRIPTOR # /home/ingres/IngresII/ingres/files/iiapi.h: 813

# /home/ingres/IngresII/ingres/files/iiapi.h: 909
class struct__IIAPI_FDATADESCR(Structure):
    pass

struct__IIAPI_FDATADESCR.__slots__ = [
    'fd_name',
    'fd_type',
    'fd_length',
    'fd_prec',
    'fd_column',
    'fd_funcID',
    'fd_cvLen',
    'fd_cvPrec',
    'fd_delimiter',
    'fd_delimLength',
    'fd_delimValue',
    'fd_nullable',
    'fd_nullInfo',
    'fd_nullDescr',
    'fd_nullValue',
]
struct__IIAPI_FDATADESCR._fields_ = [
    ('fd_name', c_char_p),
    ('fd_type', II_INT2),
    ('fd_length', II_INT2),
    ('fd_prec', II_INT2),
    ('fd_column', II_LONG),
    ('fd_funcID', II_LONG),
    ('fd_cvLen', II_LONG),
    ('fd_cvPrec', II_LONG),
    ('fd_delimiter', II_BOOL),
    ('fd_delimLength', II_INT2),
    ('fd_delimValue', c_char_p),
    ('fd_nullable', II_BOOL),
    ('fd_nullInfo', II_BOOL),
    ('fd_nullDescr', IIAPI_DESCRIPTOR),
    ('fd_nullValue', IIAPI_DATAVALUE),
]

IIAPI_FDATADESCR = struct__IIAPI_FDATADESCR # /home/ingres/IngresII/ingres/files/iiapi.h: 909

# /home/ingres/IngresII/ingres/files/iiapi.h: 965
class struct__IIAPI_COPYMAP(Structure):
    pass

struct__IIAPI_COPYMAP.__slots__ = [
    'cp_copyFrom',
    'cp_flags',
    'cp_errorCount',
    'cp_fileName',
    'cp_logName',
    'cp_dbmsCount',
    'cp_dbmsDescr',
    'cp_fileCount',
    'cp_fileDescr',
]
struct__IIAPI_COPYMAP._fields_ = [
    ('cp_copyFrom', II_BOOL),
    ('cp_flags', II_ULONG),
    ('cp_errorCount', II_LONG),
    ('cp_fileName', c_char_p),
    ('cp_logName', c_char_p),
    ('cp_dbmsCount', II_INT2),
    ('cp_dbmsDescr', POINTER(IIAPI_DESCRIPTOR)),
    ('cp_fileCount', II_INT2),
    ('cp_fileDescr', POINTER(IIAPI_FDATADESCR)),
]

IIAPI_COPYMAP = struct__IIAPI_COPYMAP # /home/ingres/IngresII/ingres/files/iiapi.h: 965

# /home/ingres/IngresII/ingres/files/iiapi.h: 1017
class struct__IIAPI_SVR_ERRINFO(Structure):
    pass

struct__IIAPI_SVR_ERRINFO.__slots__ = [
    'svr_id_error',
    'svr_local_error',
    'svr_id_server',
    'svr_server_type',
    'svr_severity',
    'svr_parmCount',
    'svr_parmDescr',
    'svr_parmValue',
]
struct__IIAPI_SVR_ERRINFO._fields_ = [
    ('svr_id_error', II_LONG),
    ('svr_local_error', II_LONG),
    ('svr_id_server', II_LONG),
    ('svr_server_type', II_LONG),
    ('svr_severity', II_LONG),
    ('svr_parmCount', II_INT2),
    ('svr_parmDescr', POINTER(IIAPI_DESCRIPTOR)),
    ('svr_parmValue', POINTER(IIAPI_DATAVALUE)),
]

IIAPI_SVR_ERRINFO = struct__IIAPI_SVR_ERRINFO # /home/ingres/IngresII/ingres/files/iiapi.h: 1017

# /home/ingres/IngresII/ingres/files/iiapi.h: 1041
class struct__IIAPI_II_TRAN_ID(Structure):
    pass

struct__IIAPI_II_TRAN_ID.__slots__ = [
    'it_highTran',
    'it_lowTran',
]
struct__IIAPI_II_TRAN_ID._fields_ = [
    ('it_highTran', II_UINT4),
    ('it_lowTran', II_UINT4),
]

IIAPI_II_TRAN_ID = struct__IIAPI_II_TRAN_ID # /home/ingres/IngresII/ingres/files/iiapi.h: 1041

# /home/ingres/IngresII/ingres/files/iiapi.h: 1068
class struct__IIAPI_II_DIS_TRAN_ID(Structure):
    pass

struct__IIAPI_II_DIS_TRAN_ID.__slots__ = [
    'ii_tranID',
    'ii_tranName',
]
struct__IIAPI_II_DIS_TRAN_ID._fields_ = [
    ('ii_tranID', IIAPI_II_TRAN_ID),
    ('ii_tranName', II_CHAR * 64),
]

IIAPI_II_DIS_TRAN_ID = struct__IIAPI_II_DIS_TRAN_ID # /home/ingres/IngresII/ingres/files/iiapi.h: 1068

# /home/ingres/IngresII/ingres/files/iiapi.h: 1102
class struct__IIAPI_XA_TRAN_ID(Structure):
    pass

struct__IIAPI_XA_TRAN_ID.__slots__ = [
    'xt_formatID',
    'xt_gtridLength',
    'xt_bqualLength',
    'xt_data',
]
struct__IIAPI_XA_TRAN_ID._fields_ = [
    ('xt_formatID', II_LONG),
    ('xt_gtridLength', II_LONG),
    ('xt_bqualLength', II_LONG),
    ('xt_data', II_CHAR * (64 + 64)),
]

IIAPI_XA_TRAN_ID = struct__IIAPI_XA_TRAN_ID # /home/ingres/IngresII/ingres/files/iiapi.h: 1102

# /home/ingres/IngresII/ingres/files/iiapi.h: 1132
class struct__IIAPI_XA_DIS_TRAN_ID(Structure):
    pass

struct__IIAPI_XA_DIS_TRAN_ID.__slots__ = [
    'xa_tranID',
    'xa_branchSeqnum',
    'xa_branchFlag',
]
struct__IIAPI_XA_DIS_TRAN_ID._fields_ = [
    ('xa_tranID', IIAPI_XA_TRAN_ID),
    ('xa_branchSeqnum', II_INT4),
    ('xa_branchFlag', II_INT4),
]

IIAPI_XA_DIS_TRAN_ID = struct__IIAPI_XA_DIS_TRAN_ID # /home/ingres/IngresII/ingres/files/iiapi.h: 1132

# /home/ingres/IngresII/ingres/files/iiapi.h: 1164
class union_anon_1(Union):
    pass

union_anon_1.__slots__ = [
    'iiXID',
    'xaXID',
]
union_anon_1._fields_ = [
    ('iiXID', IIAPI_II_DIS_TRAN_ID),
    ('xaXID', IIAPI_XA_DIS_TRAN_ID),
]

# /home/ingres/IngresII/ingres/files/iiapi.h: 1170
class struct__IIAPI_TRAN_ID(Structure):
    pass

struct__IIAPI_TRAN_ID.__slots__ = [
    'ti_type',
    'ti_value',
]
struct__IIAPI_TRAN_ID._fields_ = [
    ('ti_type', II_ULONG),
    ('ti_value', union_anon_1),
]

IIAPI_TRAN_ID = struct__IIAPI_TRAN_ID # /home/ingres/IngresII/ingres/files/iiapi.h: 1170

# /home/ingres/IngresII/ingres/files/iiapi.h: 1227
class struct__IIAPI_GENPARM(Structure):
    pass

struct__IIAPI_GENPARM.__slots__ = [
    'gp_callback',
    'gp_closure',
    'gp_completed',
    'gp_status',
    'gp_errorHandle',
]
struct__IIAPI_GENPARM._fields_ = [
    ('gp_callback', CFUNCTYPE(UNCHECKED(None), II_PTR, II_PTR)),
    ('gp_closure', II_PTR),
    ('gp_completed', II_BOOL),
    ('gp_status', IIAPI_STATUS),
    ('gp_errorHandle', II_PTR),
]

IIAPI_GENPARM = struct__IIAPI_GENPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1227

# /home/ingres/IngresII/ingres/files/iiapi.h: 1260
class struct__IIAPI_ABORTPARM(Structure):
    pass

struct__IIAPI_ABORTPARM.__slots__ = [
    'ab_genParm',
    'ab_connHandle',
]
struct__IIAPI_ABORTPARM._fields_ = [
    ('ab_genParm', IIAPI_GENPARM),
    ('ab_connHandle', II_PTR),
]

IIAPI_ABORTPARM = struct__IIAPI_ABORTPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1260

# /home/ingres/IngresII/ingres/files/iiapi.h: 1299
class struct__IIAPI_AUTOPARM(Structure):
    pass

struct__IIAPI_AUTOPARM.__slots__ = [
    'ac_genParm',
    'ac_connHandle',
    'ac_tranHandle',
]
struct__IIAPI_AUTOPARM._fields_ = [
    ('ac_genParm', IIAPI_GENPARM),
    ('ac_connHandle', II_PTR),
    ('ac_tranHandle', II_PTR),
]

IIAPI_AUTOPARM = struct__IIAPI_AUTOPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1299

# /home/ingres/IngresII/ingres/files/iiapi.h: 1330
class struct__IIAPI_CANCELPARM(Structure):
    pass

struct__IIAPI_CANCELPARM.__slots__ = [
    'cn_genParm',
    'cn_stmtHandle',
]
struct__IIAPI_CANCELPARM._fields_ = [
    ('cn_genParm', IIAPI_GENPARM),
    ('cn_stmtHandle', II_PTR),
]

IIAPI_CANCELPARM = struct__IIAPI_CANCELPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1330

# /home/ingres/IngresII/ingres/files/iiapi.h: 1400
class struct__IIAPI_CATCHEVENTPARM(Structure):
    pass

struct__IIAPI_CATCHEVENTPARM.__slots__ = [
    'ce_genParm',
    'ce_connHandle',
    'ce_selectEventName',
    'ce_selectEventOwner',
    'ce_eventHandle',
    'ce_eventName',
    'ce_eventOwner',
    'ce_eventDB',
    'ce_eventTime',
    'ce_eventInfoAvail',
]
struct__IIAPI_CATCHEVENTPARM._fields_ = [
    ('ce_genParm', IIAPI_GENPARM),
    ('ce_connHandle', II_PTR),
    ('ce_selectEventName', c_char_p),
    ('ce_selectEventOwner', c_char_p),
    ('ce_eventHandle', II_PTR),
    ('ce_eventName', c_char_p),
    ('ce_eventOwner', c_char_p),
    ('ce_eventDB', c_char_p),
    ('ce_eventTime', IIAPI_DATAVALUE),
    ('ce_eventInfoAvail', II_BOOL),
]

IIAPI_CATCHEVENTPARM = struct__IIAPI_CATCHEVENTPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1400

# /home/ingres/IngresII/ingres/files/iiapi.h: 1432
class struct__IIAPI_CLOSEPARM(Structure):
    pass

struct__IIAPI_CLOSEPARM.__slots__ = [
    'cl_genParm',
    'cl_stmtHandle',
]
struct__IIAPI_CLOSEPARM._fields_ = [
    ('cl_genParm', IIAPI_GENPARM),
    ('cl_stmtHandle', II_PTR),
]

IIAPI_CLOSEPARM = struct__IIAPI_CLOSEPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1432

# /home/ingres/IngresII/ingres/files/iiapi.h: 1465
class struct__IIAPI_COMMITPARM(Structure):
    pass

struct__IIAPI_COMMITPARM.__slots__ = [
    'cm_genParm',
    'cm_tranHandle',
]
struct__IIAPI_COMMITPARM._fields_ = [
    ('cm_genParm', IIAPI_GENPARM),
    ('cm_tranHandle', II_PTR),
]

IIAPI_COMMITPARM = struct__IIAPI_COMMITPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1465

# /home/ingres/IngresII/ingres/files/iiapi.h: 1553
class struct__IIAPI_CONNPARM(Structure):
    pass

struct__IIAPI_CONNPARM.__slots__ = [
    'co_genParm',
    'co_target',
    'co_username',
    'co_password',
    'co_timeout',
    'co_connHandle',
    'co_tranHandle',
    'co_sizeAdvise',
    'co_apiLevel',
    'co_type',
]
struct__IIAPI_CONNPARM._fields_ = [
    ('co_genParm', IIAPI_GENPARM),
    ('co_target', c_char_p),
    ('co_username', c_char_p),
    ('co_password', c_char_p),
    ('co_timeout', II_LONG),
    ('co_connHandle', II_PTR),
    ('co_tranHandle', II_PTR),
    ('co_sizeAdvise', II_LONG),
    ('co_apiLevel', II_LONG),
    ('co_type', II_LONG),
]

IIAPI_CONNPARM = struct__IIAPI_CONNPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1553

# /home/ingres/IngresII/ingres/files/iiapi.h: 1598
class struct__IIAPI_CONVERTPARM(Structure):
    pass

struct__IIAPI_CONVERTPARM.__slots__ = [
    'cv_srcDesc',
    'cv_srcValue',
    'cv_dstDesc',
    'cv_dstValue',
    'cv_status',
]
struct__IIAPI_CONVERTPARM._fields_ = [
    ('cv_srcDesc', IIAPI_DESCRIPTOR),
    ('cv_srcValue', IIAPI_DATAVALUE),
    ('cv_dstDesc', IIAPI_DESCRIPTOR),
    ('cv_dstValue', IIAPI_DATAVALUE),
    ('cv_status', IIAPI_STATUS),
]

IIAPI_CONVERTPARM = struct__IIAPI_CONVERTPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1598

# /home/ingres/IngresII/ingres/files/iiapi.h: 1647
class struct__IIAPI_FORMATPARM(Structure):
    pass

struct__IIAPI_FORMATPARM.__slots__ = [
    'fd_envHandle',
    'fd_srcDesc',
    'fd_srcValue',
    'fd_dstDesc',
    'fd_dstValue',
    'fd_status',
]
struct__IIAPI_FORMATPARM._fields_ = [
    ('fd_envHandle', II_PTR),
    ('fd_srcDesc', IIAPI_DESCRIPTOR),
    ('fd_srcValue', IIAPI_DATAVALUE),
    ('fd_dstDesc', IIAPI_DESCRIPTOR),
    ('fd_dstValue', IIAPI_DATAVALUE),
    ('fd_status', IIAPI_STATUS),
]

IIAPI_FORMATPARM = struct__IIAPI_FORMATPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1647

# /home/ingres/IngresII/ingres/files/iiapi.h: 1679
class struct__IIAPI_DISCONNPARM(Structure):
    pass

struct__IIAPI_DISCONNPARM.__slots__ = [
    'dc_genParm',
    'dc_connHandle',
]
struct__IIAPI_DISCONNPARM._fields_ = [
    ('dc_genParm', IIAPI_GENPARM),
    ('dc_connHandle', II_PTR),
]

IIAPI_DISCONNPARM = struct__IIAPI_DISCONNPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1679

# /home/ingres/IngresII/ingres/files/iiapi.h: 1730
class struct__IIAPI_GETCOLINFOPARM(Structure):
    pass

struct__IIAPI_GETCOLINFOPARM.__slots__ = [
    'gi_stmtHandle',
    'gi_columnNumber',
    'gi_status',
    'gi_mask',
    'gi_lobLength',
]
struct__IIAPI_GETCOLINFOPARM._fields_ = [
    ('gi_stmtHandle', II_PTR),
    ('gi_columnNumber', II_INT2),
    ('gi_status', IIAPI_STATUS),
    ('gi_mask', II_ULONG),
    ('gi_lobLength', II_UINT8),
]

IIAPI_GETCOLINFOPARM = struct__IIAPI_GETCOLINFOPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1730

# /home/ingres/IngresII/ingres/files/iiapi.h: 1783
class struct__IIAPI_GETCOLPARM(Structure):
    pass

struct__IIAPI_GETCOLPARM.__slots__ = [
    'gc_genParm',
    'gc_stmtHandle',
    'gc_rowCount',
    'gc_columnCount',
    'gc_columnData',
    'gc_rowsReturned',
    'gc_moreSegments',
]
struct__IIAPI_GETCOLPARM._fields_ = [
    ('gc_genParm', IIAPI_GENPARM),
    ('gc_stmtHandle', II_PTR),
    ('gc_rowCount', II_INT2),
    ('gc_columnCount', II_INT2),
    ('gc_columnData', POINTER(IIAPI_DATAVALUE)),
    ('gc_rowsReturned', II_INT2),
    ('gc_moreSegments', II_BOOL),
]

IIAPI_GETCOLPARM = struct__IIAPI_GETCOLPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1783

# /home/ingres/IngresII/ingres/files/iiapi.h: 1822
class struct__IIAPI_GETCOPYMAPPARM(Structure):
    pass

struct__IIAPI_GETCOPYMAPPARM.__slots__ = [
    'gm_genParm',
    'gm_stmtHandle',
    'gm_copyMap',
]
struct__IIAPI_GETCOPYMAPPARM._fields_ = [
    ('gm_genParm', IIAPI_GENPARM),
    ('gm_stmtHandle', II_PTR),
    ('gm_copyMap', IIAPI_COPYMAP),
]

IIAPI_GETCOPYMAPPARM = struct__IIAPI_GETCOPYMAPPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1822

# /home/ingres/IngresII/ingres/files/iiapi.h: 1864
class struct__IIAPI_GETDESCRPARM(Structure):
    pass

struct__IIAPI_GETDESCRPARM.__slots__ = [
    'gd_genParm',
    'gd_stmtHandle',
    'gd_descriptorCount',
    'gd_descriptor',
]
struct__IIAPI_GETDESCRPARM._fields_ = [
    ('gd_genParm', IIAPI_GENPARM),
    ('gd_stmtHandle', II_PTR),
    ('gd_descriptorCount', II_INT2),
    ('gd_descriptor', POINTER(IIAPI_DESCRIPTOR)),
]

IIAPI_GETDESCRPARM = struct__IIAPI_GETDESCRPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1864

# /home/ingres/IngresII/ingres/files/iiapi.h: 1926
class struct__IIAPI_GETEINFOPARM(Structure):
    pass

struct__IIAPI_GETEINFOPARM.__slots__ = [
    'ge_errorHandle',
    'ge_type',
    'ge_SQLSTATE',
    'ge_errorCode',
    'ge_message',
    'ge_serverInfoAvail',
    'ge_serverInfo',
    'ge_status',
]
struct__IIAPI_GETEINFOPARM._fields_ = [
    ('ge_errorHandle', II_PTR),
    ('ge_type', II_LONG),
    ('ge_SQLSTATE', II_CHAR * (5 + 1)),
    ('ge_errorCode', II_LONG),
    ('ge_message', c_char_p),
    ('ge_serverInfoAvail', II_BOOL),
    ('ge_serverInfo', POINTER(IIAPI_SVR_ERRINFO)),
    ('ge_status', IIAPI_STATUS),
]

IIAPI_GETEINFOPARM = struct__IIAPI_GETEINFOPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1926

# /home/ingres/IngresII/ingres/files/iiapi.h: 1962
class struct__IIAPI_GETEVENTPARM(Structure):
    pass

struct__IIAPI_GETEVENTPARM.__slots__ = [
    'gv_genParm',
    'gv_connHandle',
    'gv_timeout',
]
struct__IIAPI_GETEVENTPARM._fields_ = [
    ('gv_genParm', IIAPI_GENPARM),
    ('gv_connHandle', II_PTR),
    ('gv_timeout', II_LONG),
]

IIAPI_GETEVENTPARM = struct__IIAPI_GETEVENTPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1962

# /home/ingres/IngresII/ingres/files/iiapi.h: 2102
class struct__IIAPI_GETQINFOPARM(Structure):
    pass

struct__IIAPI_GETQINFOPARM.__slots__ = [
    'gq_genParm',
    'gq_stmtHandle',
    'gq_flags',
    'gq_mask',
    'gq_rowCount',
    'gq_readonly',
    'gq_procedureReturn',
    'gq_procedureHandle',
    'gq_repeatQueryHandle',
    'gq_tableKey',
    'gq_objectKey',
    'gq_cursorType',
    'gq_rowStatus',
    'gq_rowPosition',
]
struct__IIAPI_GETQINFOPARM._fields_ = [
    ('gq_genParm', IIAPI_GENPARM),
    ('gq_stmtHandle', II_PTR),
    ('gq_flags', II_ULONG),
    ('gq_mask', II_ULONG),
    ('gq_rowCount', II_LONG),
    ('gq_readonly', II_BOOL),
    ('gq_procedureReturn', II_LONG),
    ('gq_procedureHandle', II_PTR),
    ('gq_repeatQueryHandle', II_PTR),
    ('gq_tableKey', II_CHAR * 8),
    ('gq_objectKey', II_CHAR * 16),
    ('gq_cursorType', II_ULONG),
    ('gq_rowStatus', II_ULONG),
    ('gq_rowPosition', II_LONG),
]

IIAPI_GETQINFOPARM = struct__IIAPI_GETQINFOPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2102

# /home/ingres/IngresII/ingres/files/iiapi.h: 2159
class struct__IIAPI_INITPARM(Structure):
    pass

struct__IIAPI_INITPARM.__slots__ = [
    'in_timeout',
    'in_version',
    'in_status',
    'in_envHandle',
]
struct__IIAPI_INITPARM._fields_ = [
    ('in_timeout', II_LONG),
    ('in_version', II_LONG),
    ('in_status', IIAPI_STATUS),
    ('in_envHandle', II_PTR),
]

IIAPI_INITPARM = struct__IIAPI_INITPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2159

# /home/ingres/IngresII/ingres/files/iiapi.h: 2192
class struct__IIAPI_MODCONNPARM(Structure):
    pass

struct__IIAPI_MODCONNPARM.__slots__ = [
    'mc_genParm',
    'mc_connHandle',
]
struct__IIAPI_MODCONNPARM._fields_ = [
    ('mc_genParm', IIAPI_GENPARM),
    ('mc_connHandle', II_PTR),
]

IIAPI_MODCONNPARM = struct__IIAPI_MODCONNPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2192

# /home/ingres/IngresII/ingres/files/iiapi.h: 2238
class struct__IIAPI_POSPARM(Structure):
    pass

struct__IIAPI_POSPARM.__slots__ = [
    'po_genParm',
    'po_stmtHandle',
    'po_reference',
    'po_offset',
    'po_rowCount',
]
struct__IIAPI_POSPARM._fields_ = [
    ('po_genParm', IIAPI_GENPARM),
    ('po_stmtHandle', II_PTR),
    ('po_reference', II_UINT2),
    ('po_offset', II_INT4),
    ('po_rowCount', II_INT2),
]

IIAPI_POSPARM = struct__IIAPI_POSPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2238

# /home/ingres/IngresII/ingres/files/iiapi.h: 2270
class struct__IIAPI_PREPCMTPARM(Structure):
    pass

struct__IIAPI_PREPCMTPARM.__slots__ = [
    'pr_genParm',
    'pr_tranHandle',
]
struct__IIAPI_PREPCMTPARM._fields_ = [
    ('pr_genParm', IIAPI_GENPARM),
    ('pr_tranHandle', II_PTR),
]

IIAPI_PREPCMTPARM = struct__IIAPI_PREPCMTPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2270

# /home/ingres/IngresII/ingres/files/iiapi.h: 2312
class struct__IIAPI_PUTCOLPARM(Structure):
    pass

struct__IIAPI_PUTCOLPARM.__slots__ = [
    'pc_genParm',
    'pc_stmtHandle',
    'pc_columnCount',
    'pc_columnData',
    'pc_moreSegments',
]
struct__IIAPI_PUTCOLPARM._fields_ = [
    ('pc_genParm', IIAPI_GENPARM),
    ('pc_stmtHandle', II_PTR),
    ('pc_columnCount', II_INT2),
    ('pc_columnData', POINTER(IIAPI_DATAVALUE)),
    ('pc_moreSegments', II_BOOL),
]

IIAPI_PUTCOLPARM = struct__IIAPI_PUTCOLPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2312

# /home/ingres/IngresII/ingres/files/iiapi.h: 2353
class struct__IIAPI_PUTPARMPARM(Structure):
    pass

struct__IIAPI_PUTPARMPARM.__slots__ = [
    'pp_genParm',
    'pp_stmtHandle',
    'pp_parmCount',
    'pp_parmData',
    'pp_moreSegments',
]
struct__IIAPI_PUTPARMPARM._fields_ = [
    ('pp_genParm', IIAPI_GENPARM),
    ('pp_stmtHandle', II_PTR),
    ('pp_parmCount', II_INT2),
    ('pp_parmData', POINTER(IIAPI_DATAVALUE)),
    ('pp_moreSegments', II_BOOL),
]

IIAPI_PUTPARMPARM = struct__IIAPI_PUTPARMPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2353

# /home/ingres/IngresII/ingres/files/iiapi.h: 2421
class struct__IIAPI_QUERYPARM(Structure):
    pass

struct__IIAPI_QUERYPARM.__slots__ = [
    'qy_genParm',
    'qy_connHandle',
    'qy_queryType',
    'qy_queryText',
    'qy_parameters',
    'qy_tranHandle',
    'qy_stmtHandle',
    'qy_flags',
]
struct__IIAPI_QUERYPARM._fields_ = [
    ('qy_genParm', IIAPI_GENPARM),
    ('qy_connHandle', II_PTR),
    ('qy_queryType', IIAPI_QUERYTYPE),
    ('qy_queryText', c_char_p),
    ('qy_parameters', II_BOOL),
    ('qy_tranHandle', II_PTR),
    ('qy_stmtHandle', II_PTR),
    ('qy_flags', II_ULONG),
]

IIAPI_QUERYPARM = struct__IIAPI_QUERYPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2421

# /home/ingres/IngresII/ingres/files/iiapi.h: 2456
class struct__IIAPI_REGXIDPARM(Structure):
    pass

struct__IIAPI_REGXIDPARM.__slots__ = [
    'rg_tranID',
    'rg_tranIdHandle',
    'rg_status',
]
struct__IIAPI_REGXIDPARM._fields_ = [
    ('rg_tranID', IIAPI_TRAN_ID),
    ('rg_tranIdHandle', II_PTR),
    ('rg_status', IIAPI_STATUS),
]

IIAPI_REGXIDPARM = struct__IIAPI_REGXIDPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2456

# /home/ingres/IngresII/ingres/files/iiapi.h: 2492
class struct__IIAPI_RELXIDPARM(Structure):
    pass

struct__IIAPI_RELXIDPARM.__slots__ = [
    'rl_tranIdHandle',
    'rl_status',
]
struct__IIAPI_RELXIDPARM._fields_ = [
    ('rl_tranIdHandle', II_PTR),
    ('rl_status', IIAPI_STATUS),
]

IIAPI_RELXIDPARM = struct__IIAPI_RELXIDPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2492

# /home/ingres/IngresII/ingres/files/iiapi.h: 2524
class struct__IIAPI_RELENVPARM(Structure):
    pass

struct__IIAPI_RELENVPARM.__slots__ = [
    're_envHandle',
    're_status',
]
struct__IIAPI_RELENVPARM._fields_ = [
    ('re_envHandle', II_PTR),
    ('re_status', IIAPI_STATUS),
]

IIAPI_RELENVPARM = struct__IIAPI_RELENVPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2524

# /home/ingres/IngresII/ingres/files/iiapi.h: 2559
class struct__IIAPI_ROLLBACKPARM(Structure):
    pass

struct__IIAPI_ROLLBACKPARM.__slots__ = [
    'rb_genParm',
    'rb_tranHandle',
    'rb_savePointHandle',
]
struct__IIAPI_ROLLBACKPARM._fields_ = [
    ('rb_genParm', IIAPI_GENPARM),
    ('rb_tranHandle', II_PTR),
    ('rb_savePointHandle', II_PTR),
]

IIAPI_ROLLBACKPARM = struct__IIAPI_ROLLBACKPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2559

# /home/ingres/IngresII/ingres/files/iiapi.h: 2601
class struct__IIAPI_SAVEPTPARM(Structure):
    pass

struct__IIAPI_SAVEPTPARM.__slots__ = [
    'sp_genParm',
    'sp_tranHandle',
    'sp_savePoint',
    'sp_savePointHandle',
]
struct__IIAPI_SAVEPTPARM._fields_ = [
    ('sp_genParm', IIAPI_GENPARM),
    ('sp_tranHandle', II_PTR),
    ('sp_savePoint', c_char_p),
    ('sp_savePointHandle', II_PTR),
]

IIAPI_SAVEPTPARM = struct__IIAPI_SAVEPTPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2601

# /home/ingres/IngresII/ingres/files/iiapi.h: 2650
class struct__IIAPI_SCROLLPARM(Structure):
    pass

struct__IIAPI_SCROLLPARM.__slots__ = [
    'sl_genParm',
    'sl_stmtHandle',
    'sl_orientation',
    'sl_offset',
]
struct__IIAPI_SCROLLPARM._fields_ = [
    ('sl_genParm', IIAPI_GENPARM),
    ('sl_stmtHandle', II_PTR),
    ('sl_orientation', II_UINT2),
    ('sl_offset', II_INT4),
]

IIAPI_SCROLLPARM = struct__IIAPI_SCROLLPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2650

# /home/ingres/IngresII/ingres/files/iiapi.h: 2694
class struct__IIAPI_SETENVPRMPARM(Structure):
    pass

struct__IIAPI_SETENVPRMPARM.__slots__ = [
    'se_envHandle',
    'se_paramID',
    'se_paramValue',
    'se_status',
]
struct__IIAPI_SETENVPRMPARM._fields_ = [
    ('se_envHandle', II_PTR),
    ('se_paramID', II_LONG),
    ('se_paramValue', II_PTR),
    ('se_status', IIAPI_STATUS),
]

IIAPI_SETENVPRMPARM = struct__IIAPI_SETENVPRMPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2694

# /home/ingres/IngresII/ingres/files/iiapi.h: 2895
class struct__IIAPI_PROMPTPARM(Structure):
    pass

struct__IIAPI_PROMPTPARM.__slots__ = [
    'pd_envHandle',
    'pd_connHandle',
    'pd_flags',
    'pd_timeout',
    'pd_msg_len',
    'pd_message',
    'pd_max_reply',
    'pd_rep_flags',
    'pd_rep_len',
    'pd_reply',
]
struct__IIAPI_PROMPTPARM._fields_ = [
    ('pd_envHandle', II_PTR),
    ('pd_connHandle', II_PTR),
    ('pd_flags', II_LONG),
    ('pd_timeout', II_LONG),
    ('pd_msg_len', II_UINT2),
    ('pd_message', c_char_p),
    ('pd_max_reply', II_UINT2),
    ('pd_rep_flags', II_LONG),
    ('pd_rep_len', II_UINT2),
    ('pd_reply', c_char_p),
]

IIAPI_PROMPTPARM = struct__IIAPI_PROMPTPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2895

# /home/ingres/IngresII/ingres/files/iiapi.h: 2935
class struct__IIAPI_TRACEPARM(Structure):
    pass

struct__IIAPI_TRACEPARM.__slots__ = [
    'tr_envHandle',
    'tr_connHandle',
    'tr_length',
    'tr_message',
]
struct__IIAPI_TRACEPARM._fields_ = [
    ('tr_envHandle', II_PTR),
    ('tr_connHandle', II_PTR),
    ('tr_length', II_INT4),
    ('tr_message', c_char_p),
]

IIAPI_TRACEPARM = struct__IIAPI_TRACEPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2935

# /home/ingres/IngresII/ingres/files/iiapi.h: 2978
class struct__IIAPI_EVENTPARM(Structure):
    pass

struct__IIAPI_EVENTPARM.__slots__ = [
    'ev_envHandle',
    'ev_connHandle',
    'ev_eventName',
    'ev_eventOwner',
    'ev_eventDB',
    'ev_eventTime',
]
struct__IIAPI_EVENTPARM._fields_ = [
    ('ev_envHandle', II_PTR),
    ('ev_connHandle', II_PTR),
    ('ev_eventName', c_char_p),
    ('ev_eventOwner', c_char_p),
    ('ev_eventDB', c_char_p),
    ('ev_eventTime', IIAPI_DATAVALUE),
]

IIAPI_EVENTPARM = struct__IIAPI_EVENTPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2978

# /home/ingres/IngresII/ingres/files/iiapi.h: 3027
class struct__IIAPI_SETCONPRMPARM(Structure):
    pass

struct__IIAPI_SETCONPRMPARM.__slots__ = [
    'sc_genParm',
    'sc_connHandle',
    'sc_paramID',
    'sc_paramValue',
]
struct__IIAPI_SETCONPRMPARM._fields_ = [
    ('sc_genParm', IIAPI_GENPARM),
    ('sc_connHandle', II_PTR),
    ('sc_paramID', II_LONG),
    ('sc_paramValue', II_PTR),
]

IIAPI_SETCONPRMPARM = struct__IIAPI_SETCONPRMPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 3027

# /home/ingres/IngresII/ingres/files/iiapi.h: 3240
class struct__IIAPI_SETDESCRPARM(Structure):
    pass

struct__IIAPI_SETDESCRPARM.__slots__ = [
    'sd_genParm',
    'sd_stmtHandle',
    'sd_descriptorCount',
    'sd_descriptor',
]
struct__IIAPI_SETDESCRPARM._fields_ = [
    ('sd_genParm', IIAPI_GENPARM),
    ('sd_stmtHandle', II_PTR),
    ('sd_descriptorCount', II_INT2),
    ('sd_descriptor', POINTER(IIAPI_DESCRIPTOR)),
]

IIAPI_SETDESCRPARM = struct__IIAPI_SETDESCRPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 3240

# /home/ingres/IngresII/ingres/files/iiapi.h: 3268
class struct__IIAPI_TERMPARM(Structure):
    pass

struct__IIAPI_TERMPARM.__slots__ = [
    'tm_status',
]
struct__IIAPI_TERMPARM._fields_ = [
    ('tm_status', IIAPI_STATUS),
]

IIAPI_TERMPARM = struct__IIAPI_TERMPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 3268

# /home/ingres/IngresII/ingres/files/iiapi.h: 3300
class struct__IIAPI_WAITPARM(Structure):
    pass

struct__IIAPI_WAITPARM.__slots__ = [
    'wt_timeout',
    'wt_status',
]
struct__IIAPI_WAITPARM._fields_ = [
    ('wt_timeout', II_LONG),
    ('wt_status', IIAPI_STATUS),
]

IIAPI_WAITPARM = struct__IIAPI_WAITPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 3300

# /home/ingres/IngresII/ingres/files/iiapi.h: 3347
class struct__IIAPI_XASTARTPARM(Structure):
    pass

struct__IIAPI_XASTARTPARM.__slots__ = [
    'xs_genParm',
    'xs_connHandle',
    'xs_tranID',
    'xs_flags',
    'xs_tranHandle',
]
struct__IIAPI_XASTARTPARM._fields_ = [
    ('xs_genParm', IIAPI_GENPARM),
    ('xs_connHandle', II_PTR),
    ('xs_tranID', IIAPI_TRAN_ID),
    ('xs_flags', II_ULONG),
    ('xs_tranHandle', II_PTR),
]

IIAPI_XASTARTPARM = struct__IIAPI_XASTARTPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 3347

# /home/ingres/IngresII/ingres/files/iiapi.h: 3388
class struct__IIAPI_XAENDPARM(Structure):
    pass

struct__IIAPI_XAENDPARM.__slots__ = [
    'xe_genParm',
    'xe_connHandle',
    'xe_tranID',
    'xe_flags',
]
struct__IIAPI_XAENDPARM._fields_ = [
    ('xe_genParm', IIAPI_GENPARM),
    ('xe_connHandle', II_PTR),
    ('xe_tranID', IIAPI_TRAN_ID),
    ('xe_flags', II_ULONG),
]

IIAPI_XAENDPARM = struct__IIAPI_XAENDPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 3388

# /home/ingres/IngresII/ingres/files/iiapi.h: 3427
class struct__IIAPI_XAPREPPARM(Structure):
    pass

struct__IIAPI_XAPREPPARM.__slots__ = [
    'xp_genParm',
    'xp_connHandle',
    'xp_tranID',
    'xp_flags',
]
struct__IIAPI_XAPREPPARM._fields_ = [
    ('xp_genParm', IIAPI_GENPARM),
    ('xp_connHandle', II_PTR),
    ('xp_tranID', IIAPI_TRAN_ID),
    ('xp_flags', II_ULONG),
]

IIAPI_XAPREPPARM = struct__IIAPI_XAPREPPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 3427

# /home/ingres/IngresII/ingres/files/iiapi.h: 3468
class struct__IIAPI_XACOMMITPARM(Structure):
    pass

struct__IIAPI_XACOMMITPARM.__slots__ = [
    'xc_genParm',
    'xc_connHandle',
    'xc_tranID',
    'xc_flags',
]
struct__IIAPI_XACOMMITPARM._fields_ = [
    ('xc_genParm', IIAPI_GENPARM),
    ('xc_connHandle', II_PTR),
    ('xc_tranID', IIAPI_TRAN_ID),
    ('xc_flags', II_ULONG),
]

IIAPI_XACOMMITPARM = struct__IIAPI_XACOMMITPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 3468

# /home/ingres/IngresII/ingres/files/iiapi.h: 3507
class struct__IIAPI_XAROLLPARM(Structure):
    pass

struct__IIAPI_XAROLLPARM.__slots__ = [
    'xr_genParm',
    'xr_connHandle',
    'xr_tranID',
    'xr_flags',
]
struct__IIAPI_XAROLLPARM._fields_ = [
    ('xr_genParm', IIAPI_GENPARM),
    ('xr_connHandle', II_PTR),
    ('xr_tranID', IIAPI_TRAN_ID),
    ('xr_flags', II_ULONG),
]

# added to make handling varient types easier
class IIAPI_VARLENTYPE(Structure):
    _fields_ = [
        ('length', II_INT2),
        ('data', II_CHAR)]

IIAPI_XAROLLPARM = struct__IIAPI_XAROLLPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 3507

# /home/ingres/IngresII/ingres/files/iiapi.h: 3514
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_abort'):
        IIapi_abort = _lib.IIapi_abort
        IIapi_abort.restype = None
        IIapi_abort.argtypes = [POINTER(IIAPI_ABORTPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3517
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_autocommit'):
        IIapi_autocommit = _lib.IIapi_autocommit
        IIapi_autocommit.restype = None
        IIapi_autocommit.argtypes = [POINTER(IIAPI_AUTOPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3520
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_cancel'):
        IIapi_cancel = _lib.IIapi_cancel
        IIapi_cancel.restype = None
        IIapi_cancel.argtypes = [POINTER(IIAPI_CANCELPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3523
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_catchEvent'):
        IIapi_catchEvent = _lib.IIapi_catchEvent
        IIapi_catchEvent.restype = None
        IIapi_catchEvent.argtypes = [POINTER(IIAPI_CATCHEVENTPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3526
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_close'):
        IIapi_close = _lib.IIapi_close
        IIapi_close.restype = None
        IIapi_close.argtypes = [POINTER(IIAPI_CLOSEPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3529
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_commit'):
        IIapi_commit = _lib.IIapi_commit
        IIapi_commit.restype = None
        IIapi_commit.argtypes = [POINTER(IIAPI_COMMITPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3532
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_connect'):
        IIapi_connect = _lib.IIapi_connect
        IIapi_connect.restype = None
        IIapi_connect.argtypes = [POINTER(IIAPI_CONNPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3535
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_convertData'):
        IIapi_convertData = _lib.IIapi_convertData
        IIapi_convertData.restype = None
        IIapi_convertData.argtypes = [POINTER(IIAPI_CONVERTPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3538
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_disconnect'):
        IIapi_disconnect = _lib.IIapi_disconnect
        IIapi_disconnect.restype = None
        IIapi_disconnect.argtypes = [POINTER(IIAPI_DISCONNPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3541
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_formatData'):
        IIapi_formatData = _lib.IIapi_formatData
        IIapi_formatData.restype = None
        IIapi_formatData.argtypes = [POINTER(IIAPI_FORMATPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3544
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_getColumnInfo'):
        IIapi_getColumnInfo = _lib.IIapi_getColumnInfo
        IIapi_getColumnInfo.restype = None
        IIapi_getColumnInfo.argtypes = [POINTER(IIAPI_GETCOLINFOPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3547
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_getColumns'):
        IIapi_getColumns = _lib.IIapi_getColumns
        IIapi_getColumns.restype = None
        IIapi_getColumns.argtypes = [POINTER(IIAPI_GETCOLPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3550
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_getCopyMap'):
        IIapi_getCopyMap = _lib.IIapi_getCopyMap
        IIapi_getCopyMap.restype = None
        IIapi_getCopyMap.argtypes = [POINTER(IIAPI_GETCOPYMAPPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3553
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_getDescriptor'):
        IIapi_getDescriptor = _lib.IIapi_getDescriptor
        IIapi_getDescriptor.restype = None
        IIapi_getDescriptor.argtypes = [POINTER(IIAPI_GETDESCRPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3556
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_getErrorInfo'):
        IIapi_getErrorInfo = _lib.IIapi_getErrorInfo
        IIapi_getErrorInfo.restype = None
        IIapi_getErrorInfo.argtypes = [POINTER(IIAPI_GETEINFOPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3559
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_getEvent'):
        IIapi_getEvent = _lib.IIapi_getEvent
        IIapi_getEvent.restype = None
        IIapi_getEvent.argtypes = [POINTER(IIAPI_GETEVENTPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3562
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_getQueryInfo'):
        IIapi_getQueryInfo = _lib.IIapi_getQueryInfo
        IIapi_getQueryInfo.restype = None
        IIapi_getQueryInfo.argtypes = [POINTER(IIAPI_GETQINFOPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3565
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_initialize'):
        IIapi_initialize = _lib.IIapi_initialize
        IIapi_initialize.restype = None
        IIapi_initialize.argtypes = [POINTER(IIAPI_INITPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3568
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_modifyConnect'):
        IIapi_modifyConnect = _lib.IIapi_modifyConnect
        IIapi_modifyConnect.restype = None
        IIapi_modifyConnect.argtypes = [POINTER(IIAPI_MODCONNPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3571
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_position'):
        IIapi_position = _lib.IIapi_position
        IIapi_position.restype = None
        IIapi_position.argtypes = [POINTER(IIAPI_POSPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3574
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_prepareCommit'):
        IIapi_prepareCommit = _lib.IIapi_prepareCommit
        IIapi_prepareCommit.restype = None
        IIapi_prepareCommit.argtypes = [POINTER(IIAPI_PREPCMTPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3577
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_putColumns'):
        IIapi_putColumns = _lib.IIapi_putColumns
        IIapi_putColumns.restype = None
        IIapi_putColumns.argtypes = [POINTER(IIAPI_PUTCOLPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3580
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_putParms'):
        IIapi_putParms = _lib.IIapi_putParms
        IIapi_putParms.restype = None
        IIapi_putParms.argtypes = [POINTER(IIAPI_PUTPARMPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3583
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_query'):
        IIapi_query = _lib.IIapi_query
        IIapi_query.restype = None
        IIapi_query.argtypes = [POINTER(IIAPI_QUERYPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3586
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_registerXID'):
        IIapi_registerXID = _lib.IIapi_registerXID
        IIapi_registerXID.restype = None
        IIapi_registerXID.argtypes = [POINTER(IIAPI_REGXIDPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3589
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_releaseEnv'):
        IIapi_releaseEnv = _lib.IIapi_releaseEnv
        IIapi_releaseEnv.restype = None
        IIapi_releaseEnv.argtypes = [POINTER(IIAPI_RELENVPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3592
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_releaseXID'):
        IIapi_releaseXID = _lib.IIapi_releaseXID
        IIapi_releaseXID.restype = None
        IIapi_releaseXID.argtypes = [POINTER(IIAPI_RELXIDPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3595
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_rollback'):
        IIapi_rollback = _lib.IIapi_rollback
        IIapi_rollback.restype = None
        IIapi_rollback.argtypes = [POINTER(IIAPI_ROLLBACKPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3598
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_savePoint'):
        IIapi_savePoint = _lib.IIapi_savePoint
        IIapi_savePoint.restype = None
        IIapi_savePoint.argtypes = [POINTER(IIAPI_SAVEPTPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3601
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_scroll'):
        IIapi_scroll = _lib.IIapi_scroll
        IIapi_scroll.restype = None
        IIapi_scroll.argtypes = [POINTER(IIAPI_SCROLLPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3604
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_setConnectParam'):
        IIapi_setConnectParam = _lib.IIapi_setConnectParam
        IIapi_setConnectParam.restype = None
        IIapi_setConnectParam.argtypes = [POINTER(IIAPI_SETCONPRMPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3607
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_setDescriptor'):
        IIapi_setDescriptor = _lib.IIapi_setDescriptor
        IIapi_setDescriptor.restype = None
        IIapi_setDescriptor.argtypes = [POINTER(IIAPI_SETDESCRPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3610
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_setEnvParam'):
        IIapi_setEnvParam = _lib.IIapi_setEnvParam
        IIapi_setEnvParam.restype = None
        IIapi_setEnvParam.argtypes = [POINTER(IIAPI_SETENVPRMPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3613
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_terminate'):
        IIapi_terminate = _lib.IIapi_terminate
        IIapi_terminate.restype = None
        IIapi_terminate.argtypes = [POINTER(IIAPI_TERMPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3616
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_wait'):
        IIapi_wait = _lib.IIapi_wait
        IIapi_wait.restype = None
        IIapi_wait.argtypes = [POINTER(IIAPI_WAITPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3619
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_xaStart'):
        IIapi_xaStart = _lib.IIapi_xaStart
        IIapi_xaStart.restype = None
        IIapi_xaStart.argtypes = [POINTER(IIAPI_XASTARTPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3622
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_xaEnd'):
        IIapi_xaEnd = _lib.IIapi_xaEnd
        IIapi_xaEnd.restype = None
        IIapi_xaEnd.argtypes = [POINTER(IIAPI_XAENDPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3625
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_xaPrepare'):
        IIapi_xaPrepare = _lib.IIapi_xaPrepare
        IIapi_xaPrepare.restype = None
        IIapi_xaPrepare.argtypes = [POINTER(IIAPI_XAPREPPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3628
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_xaCommit'):
        IIapi_xaCommit = _lib.IIapi_xaCommit
        IIapi_xaCommit.restype = None
        IIapi_xaCommit.argtypes = [POINTER(IIAPI_XACOMMITPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 3631
for _lib in _libs.values():
    if hasattr(_lib, 'IIapi_xaRollback'):
        IIapi_xaRollback = _lib.IIapi_xaRollback
        IIapi_xaRollback.restype = None
        IIapi_xaRollback.argtypes = [POINTER(IIAPI_XAROLLPARM)]
        break

# /home/ingres/IngresII/ingres/files/iiapi.h: 238
try:
    TRUE = 1
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 238
try:
    FALSE = 0
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 258
try:
    II_SQLSTATE_LEN = 5
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS00000_SUCCESS = '00000'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS01000_WARNING = '01000'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS01001_CURS_OPER_CONFLICT = '01001'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS01002_DISCONNECT_ERROR = '01002'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS01003_NULL_ELIM_IN_SETFUNC = '01003'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS01004_STRING_RIGHT_TRUNC = '01004'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS01005_INSUF_DESCR_AREAS = '01005'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS01006_PRIV_NOT_REVOKED = '01006'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS01007_PRIV_NOT_GRANTED = '01007'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS01008_IMP_ZERO_BIT_PADDING = '01008'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS01009_SEARCH_COND_TOO_LONG = '01009'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS0100A_QRY_EXPR_TOO_LONG = '0100A'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS01500_LDB_TBL_NOT_DROPPED = '01500'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS01501_NO_WHERE_CLAUSE = '01501'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS02000_NO_DATA = '02000'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS07000_DSQL_ERROR = '07000'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS07001_USING_PARM_MISMATCH = '07001'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS07002_USING_TARG_MISMATCH = '07002'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS07003_CAN_EXEC_CURS_SPEC = '07003'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS07004_NEED_USING_FOR_PARMS = '07004'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS07005_STMT_NOT_CURS_SPEC = '07005'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS07006_RESTR_DT_ATTR_ERR = '07006'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS07007_NEED_USING_FOR_RES = '07007'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS07008_INV_DESCR_CNT = '07008'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS07009_INV_DESCR_IDX = '07009'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS07500_CONTEXT_MISMATCH = '07500'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS08000_CONNECTION_EXCEPTION = '08000'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS08001_CANT_GET_CONNECTION = '08001'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS08002_CONNECT_NAME_IN_USE = '08002'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS08003_NO_CONNECTION = '08003'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS08004_CONNECTION_REJECTED = '08004'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS08006_CONNECTION_FAILURE = '08006'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS08007_XACT_RES_UNKNOWN = '08007'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS08500_LDB_UNAVAILABLE = '08500'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS0A000_FEATUR_NOT_SUPPORTED = '0A000'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS0A001_MULT_SERVER_XACTS = '0A001'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS0A500_INVALID_QRY_LANG = '0A500'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS21000_CARD_VIOLATION = '21000'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS22000_DATA_EXCEPTION = '22000'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS22001_STRING_RIGHT_TRUNC = '22001'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS22002_NULLVAL_NO_IND_PARAM = '22002'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS22003_NUM_VAL_OUT_OF_RANGE = '22003'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS22005_ASSIGNMENT_ERROR = '22005'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS22007_INV_DATETIME_FMT = '22007'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS22008_DATETIME_FLD_OVFLOW = '22008'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS22009_INV_TZ_DISPL_VAL = '22009'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS22011_SUBSTRING_ERROR = '22011'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS22012_DIVISION_BY_ZERO = '22012'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS22015_INTERVAL_FLD_OVFLOW = '22015'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS22018_INV_VAL_FOR_CAST = '22018'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS22019_INV_ESCAPE_CHAR = '22019'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS22021_CHAR_NOT_IN_RPRTR = '22021'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS22022_INDICATOR_OVFLOW = '22022'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS22023_INV_PARAM_VAL = '22023'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS22024_UNTERM_C_STRING = '22024'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS22025_INV_ESCAPE_SEQ = '22025'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS22026_STRING_LEN_MISMATCH = '22026'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS22027_TRIM_ERROR = '22027'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS22500_INVALID_DATA_TYPE = '22500'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS23000_CONSTR_VIOLATION = '23000'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS23501_UNIQUE_CONS_VIOLATION = '23501'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS24000_INV_CURS_STATE = '24000'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS25000_INV_XACT_STATE = '25000'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS26000_INV_SQL_STMT_NAME = '26000'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS27000_TRIG_DATA_CHNG_ERR = '27000'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS28000_INV_AUTH_SPEC = '28000'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS2A500_TBL_NOT_FOUND = '2A500'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS2A501_COL_NOT_FOUND = '2A501'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS2A502_DUPL_OBJECT = '2A502'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS2A503_INSUF_PRIV = '2A503'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS2A504_UNKNOWN_CURSOR = '2A504'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS2A505_OBJ_NOT_FOUND = '2A505'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS2A506_INVALID_IDENTIFIER = '2A506'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS2A507_RESERVED_IDENTIFIER = '2A507'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS2B000_DEP_PRIV_EXISTS = '2B000'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS2C000_INV_CH_SET_NAME = '2C000'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS2D000_INV_XACT_TERMINATION = '2D000'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS2E000_INV_CONN_NAME = '2E000'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS33000_INV_SQL_DESCR_NAME = '33000'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS34000_INV_CURS_NAME = '34000'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS35000_INV_COND_NUM = '35000'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS37500_TBL_NOT_FOUND = '37500'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS37501_COL_NOT_FOUND = '37501'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS37502_DUPL_OBJECT = '37502'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS37503_INSUF_PRIV = '37503'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS37504_UNKNOWN_CURSOR = '37504'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS37505_OBJ_NOT_FOUND = '37505'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS37506_INVALID_IDENTIFIER = '37506'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS37507_RESERVED_IDENTIFIER = '37507'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS3C000_AMBIG_CURS_NAME = '3C000'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS3D000_INV_CAT_NAME = '3D000'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS3F000_INV_SCHEMA_NAME = '3F000'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS40000_XACT_ROLLBACK = '40000'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS40001_SERIALIZATION_FAIL = '40001'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS40002_CONSTR_VIOLATION = '40002'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS40003_STMT_COMPL_UNKNOWN = '40003'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS42000_SYN_OR_ACCESSERR = '42000'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS42500_TBL_NOT_FOUND = '42500'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS42501_COL_NOT_FOUND = '42501'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS42502_DUPL_OBJECT = '42502'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS42503_INSUF_PRIV = '42503'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS42504_UNKNOWN_CURSOR = '42504'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS42505_OBJ_NOT_FOUND = '42505'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS42506_INVALID_IDENTIFIER = '42506'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS42507_RESERVED_IDENTIFIER = '42507'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS44000_CHECK_OPTION_ERR = '44000'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS50000_MISC_ING_ERRORS = '50000'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS50001_INVALID_DUP_ROW = '50001'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS50002_LIMIT_EXCEEDED = '50002'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS50003_EXHAUSTED_RESOURCE = '50003'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS50004_SYS_CONFIG_ERROR = '50004'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS50005_GW_ERROR = '50005'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS50006_FATAL_ERROR = '50006'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS50007_INVALID_SQL_STMT_ID = '50007'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS50008_UNSUPPORTED_STMT = '50008'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS50009_ERROR_RAISED_IN_DBPROC = '50009'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS5000A_QUERY_ERROR = '5000A'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS5000B_INTERNAL_ERROR = '5000B'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS5000C_FETCH_ORIENTATION = '5000C'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS5000D_INVALID_CURSOR_NAME = '5000D'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS5000E_DUP_STMT_ID = '5000E'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS5000F_TEXTUAL_INFO = '5000F'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS5000G_DBPROC_MESSAGE = '5000G'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS5000H_UNAVAILABLE_RESOURCE = '5000H'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS5000I_UNEXP_LDB_SCHEMA_CHNG = '5000I'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS5000J_INCONSISTENT_DBMS_CAT = '5000J'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS5000K_SQLSTATE_UNAVAILABLE = '5000K'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS5000L_PROTOCOL_ERROR = '5000L'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS5000M_IPC_ERROR = '5000M'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS5000N_OPERAND_TYPE_MISMATCH = '5000N'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS5000O_INVALID_FUNC_ARG_TYPE = '5000O'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS5000P_TIMEOUT_ON_LOCK_REQUEST = '5000P'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS5000Q_DB_REORG_INVALIDATED_QP = '5000Q'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SS5000R_RUN_TIME_LOGICAL_ERROR = '5000R'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 259
try:
    II_SSHZ000_RDA = 'HZ000'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 422
try:
    E_AP_MASK = (201 * 65536)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP0000_OK = 0
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP0001_CONNECTION_ABORTED = (E_AP_MASK + 1)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP0002_TRANSACTION_ABORTED = (E_AP_MASK + 2)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP0003_ACTIVE_TRANSACTIONS = (E_AP_MASK + 3)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP0004_ACTIVE_QUERIES = (E_AP_MASK + 4)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP0005_ACTIVE_EVENTS = (E_AP_MASK + 5)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP0006_INVALID_SEQUENCE = (E_AP_MASK + 6)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP0007_INCOMPLETE_QUERY = (E_AP_MASK + 7)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP0008_QUERY_DONE = (E_AP_MASK + 8)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP0009_QUERY_CANCELLED = (E_AP_MASK + 9)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP000A_QUERY_INTERRUPTED = (E_AP_MASK + 10)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP000B_COMMIT_FAILED = (E_AP_MASK + 11)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP000C_2PC_REFUSED = (E_AP_MASK + 12)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP000D_PARAMETERS_REQUIRED = (E_AP_MASK + 13)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP000E_INVALID_CONNECT_PARM = (E_AP_MASK + 14)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP000F_NO_CONNECT_PARMS = (E_AP_MASK + 15)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP0010_INVALID_COLUMN_COUNT = (E_AP_MASK + 16)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP0011_INVALID_PARAM_VALUE = (E_AP_MASK + 17)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP0012_INVALID_DESCR_INFO = (E_AP_MASK + 18)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP0013_INVALID_POINTER = (E_AP_MASK + 19)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP0014_INVALID_REPEAT_ID = (E_AP_MASK + 20)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP0015_INVALID_TRANS_STMT = (E_AP_MASK + 21)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP0016_ROW_DISCARDED = (E_AP_MASK + 22)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP0017_SEGMENT_DISCARDED = (E_AP_MASK + 23)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP0018_INVALID_DISCONNECT = (E_AP_MASK + 24)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP0020_BYREF_UNSUPPORTED = (E_AP_MASK + 32)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP0021_GTT_UNSUPPORTED = (E_AP_MASK + 33)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP0022_XA_UNSUPPORTED = (E_AP_MASK + 34)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP0023_INVALID_NULL_DATA = (E_AP_MASK + 35)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP0024_INVALID_DATA_SIZE = (E_AP_MASK + 36)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP0025_SVC_DATA_TYPE = (E_AP_MASK + 37)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP0028_LVL1_DATA_TYPE = (E_AP_MASK + 40)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP0029_LVL2_DATA_TYPE = (E_AP_MASK + 41)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP002A_LVL3_DATA_TYPE = (E_AP_MASK + 42)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP002B_LVL4_DATA_TYPE = (E_AP_MASK + 43)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 423
try:
    E_AP002C_LVL5_DATA_TYPE = (E_AP_MASK + 44)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 473
try:
    IIAPI_XAER_ASYNC = (-2)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 473
try:
    IIAPI_XAER_RMERR = (-3)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 473
try:
    IIAPI_XAER_NOTA = (-4)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 473
try:
    IIAPI_XAER_INVAL = (-5)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 473
try:
    IIAPI_XAER_PROTO = (-6)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 473
try:
    IIAPI_XAER_RMFAIL = (-7)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 473
try:
    IIAPI_XAER_DUPID = (-8)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 473
try:
    IIAPI_XAER_OUTSIDE = (-9)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 474
try:
    IIAPI_XA_RDONLY = 3
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 474
try:
    IIAPI_XA_RETRY = 4
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 474
try:
    IIAPI_XA_HEURMIX = 5
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 474
try:
    IIAPI_XA_HEURRB = 6
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 474
try:
    IIAPI_XA_HEURCOM = 7
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 474
try:
    IIAPI_XA_HEURHAZ = 8
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 474
try:
    IIAPI_XA_NOMIGRATE = 9
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 475
try:
    IIAPI_XA_RBROLLBACK = 100
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 475
try:
    IIAPI_XA_RBCOMMFAIL = 101
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 475
try:
    IIAPI_XA_RBDEADLOCK = 102
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 475
try:
    IIAPI_XA_RBINTEGRITY = 103
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 475
try:
    IIAPI_XA_RBOTHER = 104
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 475
try:
    IIAPI_XA_RBPROTO = 105
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 475
try:
    IIAPI_XA_RBTIMEOUT = 106
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 475
try:
    IIAPI_XA_RBTRANSIENT = 107
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 481
try:
    IIAPI_MIB_TRACE_LEVEL = 'exp.aif.api.trace_level'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 481
try:
    IIAPI_MIB_CONN = 'exp.aif.api.conn'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 481
try:
    IIAPI_MIB_CONN_TARGET = 'exp.aif.api.conn.target'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 481
try:
    IIAPI_MIB_CONN_USERID = 'exp.aif.api.conn.userid'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 481
try:
    IIAPI_MIB_CONN_GCA_ASSOC = 'exp.aif.api.conn.gca_assoc'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_HNDL_TYPE = (-1)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_CHR_TYPE = 32
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_CHA_TYPE = 20
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_VCH_TYPE = 21
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_LVCH_TYPE = 22
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_LCLOC_TYPE = 36
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_BYTE_TYPE = 23
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_VBYTE_TYPE = 24
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_LBYTE_TYPE = 25
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_LBLOC_TYPE = 35
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_NCHA_TYPE = 26
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_NVCH_TYPE = 27
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_LNVCH_TYPE = 28
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_LNLOC_TYPE = 29
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_TXT_TYPE = 37
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_LTXT_TYPE = 41
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_INT_TYPE = 30
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_FLT_TYPE = 31
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_MNY_TYPE = 5
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_DEC_TYPE = 10
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_DTE_TYPE = 3
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_DATE_TYPE = 4
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_TIME_TYPE = 8
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_TMWO_TYPE = 6
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_TMTZ_TYPE = 7
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_TS_TYPE = 19
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_TSWO_TYPE = 9
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_TSTZ_TYPE = 18
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_INTYM_TYPE = 33
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_INTDS_TYPE = 34
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_LOGKEY_TYPE = 11
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 532
try:
    IIAPI_TABKEY_TYPE = 12
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 533
try:
    IIAPI_IDATE_TYPE = IIAPI_DTE_TYPE
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 533
try:
    IIAPI_ADATE_TYPE = IIAPI_DATE_TYPE
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 534
try:
    IIAPI_I1_LEN = 1
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 534
try:
    IIAPI_I2_LEN = 2
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 534
try:
    IIAPI_I4_LEN = 4
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 534
try:
    IIAPI_I8_LEN = 8
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 534
try:
    IIAPI_F4_LEN = 4
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 534
try:
    IIAPI_F8_LEN = 8
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 534
try:
    IIAPI_MNY_LEN = 8
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 534
try:
    IIAPI_DTE_LEN = 12
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 534
try:
    IIAPI_TIME_LEN = 10
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 534
try:
    IIAPI_DATE_LEN = 4
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 534
try:
    IIAPI_TS_LEN = 14
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 534
try:
    IIAPI_INTYM_LEN = 3
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 534
try:
    IIAPI_INTDS_LEN = 12
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 534
try:
    IIAPI_LOGKEY_LEN = 16
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 534
try:
    IIAPI_TABKEY_LEN = 8
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 534
try:
    IIAPI_LOCATOR_LEN = 4
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 535
try:
    IIAPI_IDATE_LEN = IIAPI_DTE_LEN
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 535
try:
    IIAPI_ADATE_LEN = IIAPI_DATE_LEN
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 541
try:
    IIAPI_SEGMENT_LEN = 2000
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 620
try:
    IIAPI_ST_SUCCESS = 0
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 620
try:
    IIAPI_ST_MESSAGE = 1
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 620
try:
    IIAPI_ST_WARNING = 2
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 620
try:
    IIAPI_ST_NO_DATA = 3
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 620
try:
    IIAPI_ST_ERROR = 4
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 620
try:
    IIAPI_ST_FAILURE = 5
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 620
try:
    IIAPI_ST_NOT_INITIALIZED = 6
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 620
try:
    IIAPI_ST_INVALID_HANDLE = 7
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 620
try:
    IIAPI_ST_OUT_OF_MEMORY = 8
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 651
try:
    IIAPI_QT_BASE = 0
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 651
try:
    IIAPI_QT_QUERY = (IIAPI_QT_BASE + 0)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 651
try:
    IIAPI_QT_SELECT_SINGLETON = (IIAPI_QT_BASE + 1)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 651
try:
    IIAPI_QT_EXEC = (IIAPI_QT_BASE + 2)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 651
try:
    IIAPI_QT_OPEN = (IIAPI_QT_BASE + 3)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 651
try:
    IIAPI_QT_CURSOR_DELETE = (IIAPI_QT_BASE + 4)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 651
try:
    IIAPI_QT_CURSOR_UPDATE = (IIAPI_QT_BASE + 5)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 651
try:
    IIAPI_QT_DEF_REPEAT_QUERY = (IIAPI_QT_BASE + 6)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 651
try:
    IIAPI_QT_EXEC_REPEAT_QUERY = (IIAPI_QT_BASE + 7)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 651
try:
    IIAPI_QT_EXEC_PROCEDURE = (IIAPI_QT_BASE + 8)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 651
try:
    IIAPI_QT_TOP = IIAPI_QT_EXEC_PROCEDURE
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_ALTER_GROUP = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_ALTER_ROLE = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_ALTER_TABLE = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_COPY_FROM = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_COPY_INTO = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_CREATE_DBEVENT = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_CREATE_GROUP = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_CREATE_INDEX = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_CREATE_INTEGRITY = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_CREATE_PROCEDURE = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_CREATE_ROLE = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_CREATE_RULE = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_CREATE_TABLE = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_CREATE_VIEW = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_DELETE = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_DESCRIBE = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_DIRECT_EXEC = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_DROP_DBEVENT = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_DROP_GROUP = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_DROP_INDEX = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_DROP_INTEGRITY = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_DROP_PERMIT = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_DROP_PROCEDURE = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_DROP_ROLE = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_DROP_RULE = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_DROP_TABLE = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_DROP_VIEW = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_EXEC_IMMEDIATE = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_GRANT = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_GET_DBEVENT = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_INSERT_INTO = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_MODIFY = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_PREPARE = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_RAISE_DBEVENT = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_REGISTER_DBEVENT = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_REMOVE_DBEVENT = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_REVOKE = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_SAVE_TABLE = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_SELECT = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_SET = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 652
try:
    IIAPI_QT_UPDATE = IIAPI_QT_QUERY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 800
try:
    IIAPI_COL_TUPLE = 0
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 800
try:
    IIAPI_COL_PROCBYREFPARM = 1
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 800
try:
    IIAPI_COL_PROCPARM = 2
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 800
try:
    IIAPI_COL_SVCPARM = 3
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 800
try:
    IIAPI_COL_QPARM = 4
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 800
try:
    IIAPI_COL_PROCGTTPARM = 5
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 801
try:
    IIAPI_COL_PROCINPARM = 2
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 801
try:
    IIAPI_COL_PROCOUTPARM = 6
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 801
try:
    IIAPI_COL_PROCINOUTPARM = 1
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 1008
try:
    IIAPI_SVR_DEFAULT = 0
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 1008
try:
    IIAPI_SVR_MESSAGE = 1
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 1008
try:
    IIAPI_SVR_WARNING = 2
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 1008
try:
    IIAPI_SVR_FORMATTED = 16
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 1064
try:
    IIAPI_TRAN_MAXNAME = 64
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 1090
try:
    IIAPI_XA_MAXGTRIDSIZE = 64
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 1090
try:
    IIAPI_XA_MAXBQUALSIZE = 64
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 1090
try:
    IIAPI_XA_XIDDATASIZE = (IIAPI_XA_MAXGTRIDSIZE + IIAPI_XA_MAXBQUALSIZE)
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 1126
try:
    IIAPI_XA_BRANCH_FLAG_NOOP = 0
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 1126
try:
    IIAPI_XA_BRANCH_FLAG_FIRST = 1
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 1126
try:
    IIAPI_XA_BRANCH_FLAG_LAST = 2
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 1126
try:
    IIAPI_XA_BRANCH_FLAG_2PC = 4
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 1126
try:
    IIAPI_XA_BRANCH_FLAG_1PC = 8
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 1161
try:
    IIAPI_TI_IIXID = 1
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 1161
try:
    IIAPI_TI_XAXID = 2
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 1539
try:
    IIAPI_LEVEL_0 = 0
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 1539
try:
    IIAPI_LEVEL_1 = 1
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 1539
try:
    IIAPI_LEVEL_2 = 2
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 1539
try:
    IIAPI_LEVEL_3 = 3
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 1539
try:
    IIAPI_LEVEL_4 = 4
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 1539
try:
    IIAPI_LEVEL_5 = 5
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 1544
try:
    IIAPI_CT_SQL = 1
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 1544
try:
    IIAPI_CT_NS = 3
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 1726
try:
    IIAPI_GI_LOB_LENGTH = 1
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 1912
try:
    IIAPI_GE_ERROR = 1
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 1912
try:
    IIAPI_GE_WARNING = 2
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 1912
try:
    IIAPI_GE_MESSAGE = 3
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 1912
try:
    IIAPI_GE_XAERR = 4
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2044
try:
    IIAPI_GQF_FAIL = 1
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2044
try:
    IIAPI_GQF_ALL_UPDATED = 2
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2044
try:
    IIAPI_GQF_NULLS_REMOVED = 4
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2044
try:
    IIAPI_GQF_UNKNOWN_REPEAT_QUERY = 8
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2044
try:
    IIAPI_GQF_END_OF_DATA = 16
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2044
try:
    IIAPI_GQF_CONTINUE = 32
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2044
try:
    IIAPI_GQF_INVALID_STATEMENT = 64
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2044
try:
    IIAPI_GQF_TRANSACTION_INACTIVE = 128
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2044
try:
    IIAPI_GQF_OBJECT_KEY = 256
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2044
try:
    IIAPI_GQF_TABLE_KEY = 512
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2044
try:
    IIAPI_GQF_NEW_EFFECTIVE_USER = 1024
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2044
try:
    IIAPI_GQF_FLUSH_QUERY_ID = 2048
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2044
try:
    IIAPI_GQF_ILLEGAL_XACT_STMT = 4096
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2047
try:
    IIAPI_GQ_ROW_COUNT = 1
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2047
try:
    IIAPI_GQ_CURSOR = 2
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2047
try:
    IIAPI_GQ_PROCEDURE_RET = 4
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2047
try:
    IIAPI_GQ_PROCEDURE_ID = 8
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2047
try:
    IIAPI_GQ_REPEAT_QUERY_ID = 16
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2047
try:
    IIAPI_GQ_TABLE_KEY = 32
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2047
try:
    IIAPI_GQ_OBJECT_KEY = 64
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2047
try:
    IIAPI_GQ_ROW_STATUS = 128
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2054
try:
    IIAPI_TBLKEYSZ = 8
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2057
try:
    IIAPI_OBJKEYSZ = 16
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2064
try:
    IIAPI_CURSOR_UPDATE = 1
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2064
try:
    IIAPI_CURSOR_SCROLL = 2
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2067
try:
    IIAPI_ROW_BEFORE = 1
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2067
try:
    IIAPI_ROW_FIRST = 2
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2067
try:
    IIAPI_ROW_LAST = 4
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2067
try:
    IIAPI_ROW_AFTER = 8
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2067
try:
    IIAPI_ROW_INSERTED = 16
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2067
try:
    IIAPI_ROW_UPDATED = 32
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2067
try:
    IIAPI_ROW_DELETED = 64
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2143
try:
    IIAPI_VERSION_1 = 1
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2143
try:
    IIAPI_VERSION_2 = 2
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2143
try:
    IIAPI_VERSION_3 = 3
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2143
try:
    IIAPI_VERSION_4 = 4
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2143
try:
    IIAPI_VERSION_5 = 5
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2143
try:
    IIAPI_VERSION_6 = 6
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2143
try:
    IIAPI_VERSION = IIAPI_VERSION_6
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2231
try:
    IIAPI_POS_BEGIN = 1
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2231
try:
    IIAPI_POS_END = 2
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2231
try:
    IIAPI_POS_CURRENT = 3
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2418
try:
    IIAPI_QF_LOCATORS = 1
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2418
try:
    IIAPI_QF_SCROLL = 2
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2638
try:
    IIAPI_SCROLL_BEFORE = 1
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2638
try:
    IIAPI_SCROLL_FIRST = 2
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2638
try:
    IIAPI_SCROLL_PRIOR = 3
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2638
try:
    IIAPI_SCROLL_CURRENT = 4
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2638
try:
    IIAPI_SCROLL_NEXT = 5
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2638
try:
    IIAPI_SCROLL_LAST = 6
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2638
try:
    IIAPI_SCROLL_AFTER = 7
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2638
try:
    IIAPI_SCROLL_ABSOLUTE = 8
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2638
try:
    IIAPI_SCROLL_RELATIVE = 9
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2707
try:
    IIAPI_EP_CHAR_WIDTH = 1
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2709
try:
    IIAPI_EP_TXT_WIDTH = 2
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2711
try:
    IIAPI_EP_INT1_WIDTH = 3
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2713
try:
    IIAPI_EP_INT2_WIDTH = 4
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2715
try:
    IIAPI_EP_INT4_WIDTH = 5
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2717
try:
    IIAPI_EP_INT8_WIDTH = 28
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2719
try:
    IIAPI_EP_FLOAT4_WIDTH = 6
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2721
try:
    IIAPI_EP_FLOAT8_WIDTH = 7
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2723
try:
    IIAPI_EP_FLOAT4_PRECISION = 8
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2725
try:
    IIAPI_EP_FLOAT8_PRECISION = 9
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2727
try:
    IIAPI_EP_MONEY_PRECISION = 10
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2729
try:
    IIAPI_EP_FLOAT4_STYLE = 11
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2730
try:
    IIAPI_EPV_EXPONENTIAL = 'e'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2730
try:
    IIAPI_EPV_FLOATF = 'f'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2730
try:
    IIAPI_EPV_FLOATDEC = 'n'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2730
try:
    IIAPI_EPV_FLOATDECALIGN = 'g'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2732
try:
    IIAPI_EP_FLOAT8_STYLE = 12
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2734
try:
    IIAPI_EP_NUMERIC_TREATMENT = 13
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2735
try:
    IIAPI_EPV_DECASFLOAT = 'f'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2735
try:
    IIAPI_EPV_DECASDEC = 'd'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2737
try:
    IIAPI_EP_MONEY_SIGN = 14
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2739
try:
    IIAPI_EP_MONEY_LORT = 15
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2740
try:
    IIAPI_EPV_MONEY_LEAD_SIGN = 0
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2740
try:
    IIAPI_EPV_MONEY_TRAIL_SIGN = 1
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2742
try:
    IIAPI_EP_DECIMAL_CHAR = 16
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2744
try:
    IIAPI_EP_MATH_EXCP = 17
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2745
try:
    IIAPI_EPV_RET_FATAL = 'fail'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2745
try:
    IIAPI_EPV_RET_WARN = 'warn'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2745
try:
    IIAPI_EPV_RET_IGNORE = 'ignore'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2747
try:
    IIAPI_EP_STRING_TRUNC = 18
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2749
try:
    IIAPI_EP_DATE_FORMAT = 19
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2750
try:
    IIAPI_EPV_DFRMT_US = 0
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2750
try:
    IIAPI_EPV_DFRMT_MULTI = 1
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2750
try:
    IIAPI_EPV_DFRMT_FINNISH = 2
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2750
try:
    IIAPI_EPV_DFRMT_ISO = 3
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2750
try:
    IIAPI_EPV_DFRMT_GERMAN = 4
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2750
try:
    IIAPI_EPV_DFRMT_YMD = 5
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2750
try:
    IIAPI_EPV_DFRMT_MDY = 6
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2750
try:
    IIAPI_EPV_DFRMT_DMY = 7
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2750
try:
    IIAPI_EPV_DFRMT_MLT4 = 8
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2750
try:
    IIAPI_EPV_DFRMT_ISO4 = 9
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2752
try:
    IIAPI_EP_TIMEZONE = 20
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2754
try:
    IIAPI_EP_NATIVE_LANG = 21
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2756
try:
    IIAPI_EP_NATIVE_LANG_CODE = 22
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2758
try:
    IIAPI_EP_CENTURY_BOUNDARY = 23
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2760
try:
    IIAPI_EP_MAX_SEGMENT_LEN = 24
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2762
try:
    IIAPI_EP_TRACE_FUNC = 25
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2764
try:
    IIAPI_EP_PROMPT_FUNC = 26
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2766
try:
    IIAPI_EP_EVENT_FUNC = 27
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2770
try:
    IIAPI_EP_DATE_ALIAS = 29
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2771
try:
    IIAPI_EPV_INGDATE = 'ingresdate'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2771
try:
    IIAPI_EPV_ANSIDATE = 'ansidate'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2772
try:
    IIAPI_EP_BASE = IIAPI_EP_CHAR_WIDTH
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2772
try:
    IIAPI_EP_TOP = IIAPI_EP_DATE_ALIAS
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2878
try:
    IIAPI_PR_NOECHO = 1
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2878
try:
    IIAPI_PR_TIMEOUT = 2
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 2888
try:
    IIAPI_REPLY_TIMEOUT = 1
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3039
try:
    IIAPI_CP_CHAR_WIDTH = 1
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3041
try:
    IIAPI_CP_TXT_WIDTH = 2
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3043
try:
    IIAPI_CP_INT1_WIDTH = 3
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3045
try:
    IIAPI_CP_INT2_WIDTH = 4
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3047
try:
    IIAPI_CP_INT4_WIDTH = 5
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3049
try:
    IIAPI_CP_INT8_WIDTH = 39
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3051
try:
    IIAPI_CP_FLOAT4_WIDTH = 6
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3053
try:
    IIAPI_CP_FLOAT8_WIDTH = 7
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3055
try:
    IIAPI_CP_FLOAT4_PRECISION = 8
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3057
try:
    IIAPI_CP_FLOAT8_PRECISION = 9
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3059
try:
    IIAPI_CP_MONEY_PRECISION = 10
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3061
try:
    IIAPI_CP_FLOAT4_STYLE = 11
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3062
try:
    IIAPI_CPV_EXPONENTIAL = IIAPI_EPV_EXPONENTIAL
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3062
try:
    IIAPI_CPV_FLOATF = IIAPI_EPV_FLOATF
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3062
try:
    IIAPI_CPV_FLOATDEC = IIAPI_EPV_FLOATDEC
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3062
try:
    IIAPI_CPV_FLOATDECALIGN = IIAPI_EPV_FLOATDECALIGN
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3064
try:
    IIAPI_CP_FLOAT8_STYLE = 12
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3066
try:
    IIAPI_CP_NUMERIC_TREATMENT = 13
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3067
try:
    IIAPI_CPV_DECASFLOAT = IIAPI_EPV_DECASFLOAT
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3067
try:
    IIAPI_CPV_DECASDEC = IIAPI_EPV_DECASDEC
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3069
try:
    IIAPI_CP_MONEY_SIGN = 14
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3071
try:
    IIAPI_CP_MONEY_LORT = 15
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3072
try:
    IIAPI_CPV_MONEY_LEAD_SIGN = IIAPI_EPV_MONEY_LEAD_SIGN
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3072
try:
    IIAPI_CPV_MONEY_TRAIL_SIGN = IIAPI_EPV_MONEY_TRAIL_SIGN
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3074
try:
    IIAPI_CP_DECIMAL_CHAR = 16
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3076
try:
    IIAPI_CP_MATH_EXCP = 17
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3077
try:
    IIAPI_CPV_RET_FATAL = IIAPI_EPV_RET_FATAL
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3077
try:
    IIAPI_CPV_RET_WARN = IIAPI_EPV_RET_WARN
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3077
try:
    IIAPI_CPV_RET_IGNORE = IIAPI_EPV_RET_IGNORE
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3079
try:
    IIAPI_CP_STRING_TRUNC = 18
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3081
try:
    IIAPI_CP_DATE_FORMAT = 19
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3082
try:
    IIAPI_CPV_DFRMT_US = IIAPI_EPV_DFRMT_US
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3082
try:
    IIAPI_CPV_DFRMT_MULTI = IIAPI_EPV_DFRMT_MULTI
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3082
try:
    IIAPI_CPV_DFRMT_FINNISH = IIAPI_EPV_DFRMT_FINNISH
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3082
try:
    IIAPI_CPV_DFRMT_ISO = IIAPI_EPV_DFRMT_ISO
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3082
try:
    IIAPI_CPV_DFRMT_GERMAN = IIAPI_EPV_DFRMT_GERMAN
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3082
try:
    IIAPI_CPV_DFRMT_YMD = IIAPI_EPV_DFRMT_YMD
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3082
try:
    IIAPI_CPV_DFRMT_MDY = IIAPI_EPV_DFRMT_MDY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3082
try:
    IIAPI_CPV_DFRMT_DMY = IIAPI_EPV_DFRMT_DMY
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3082
try:
    IIAPI_CPV_DFRMT_MLT4 = IIAPI_EPV_DFRMT_MLT4
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3082
try:
    IIAPI_CPV_DFRMT_ISO4 = IIAPI_EPV_DFRMT_ISO4
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3084
try:
    IIAPI_CP_TIMEZONE = 20
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3086
try:
    IIAPI_CP_SECONDARY_INX = 21
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3087
try:
    IIAPI_CPV_ISAM = 'isam'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3087
try:
    IIAPI_CPV_CISAM = 'cisam'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3087
try:
    IIAPI_CPV_BTREE = 'btree'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3087
try:
    IIAPI_CPV_CBTREE = 'cbtree'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3087
try:
    IIAPI_CPV_HEAP = 'heap'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3087
try:
    IIAPI_CPV_CHEAP = 'cheap'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3087
try:
    IIAPI_CPV_HASH = 'hash'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3087
try:
    IIAPI_CPV_CHASH = 'chash'
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3089
try:
    IIAPI_CP_RESULT_TBL = 22
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3091
try:
    IIAPI_CP_SERVER_TYPE = 23
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3092
try:
    IIAPI_CPV_SVNORMAL = 0
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3092
try:
    IIAPI_CPV_MONITOR = 1
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3094
try:
    IIAPI_CP_NATIVE_LANG = 24
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3096
try:
    IIAPI_CP_NATIVE_LANG_CODE = 25
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3098
try:
    IIAPI_CP_APPLICATION = 26
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3100
try:
    IIAPI_CP_APP_ID = 27
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3102
try:
    IIAPI_CP_GROUP_ID = 28
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3104
try:
    IIAPI_CP_EFFECTIVE_USER = 29
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3106
try:
    IIAPI_CP_EXCLUSIVE_SYS_UPDATE = 30
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3108
try:
    IIAPI_CP_SHARED_SYS_UPDATE = 31
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3110
try:
    IIAPI_CP_EXCLUSIVE_LOCK = 32
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3112
try:
    IIAPI_CP_WAIT_LOCK = 33
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3114
try:
    IIAPI_CP_MISC_PARM = 34
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3116
try:
    IIAPI_CP_GATEWAY_PARM = 35
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3118
try:
    IIAPI_CP_DBMS_PASSWORD = 36
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3120
try:
    IIAPI_CP_CENTURY_BOUNDARY = 37
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3122
try:
    IIAPI_CP_LOGIN_LOCAL = 38
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3126
try:
    IIAPI_CP_DATE_ALIAS = 40
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3127
try:
    IIAPI_CPV_INGDATE = IIAPI_EPV_INGDATE
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3127
try:
    IIAPI_CPV_ANSIDATE = IIAPI_EPV_ANSIDATE
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3128
try:
    IIAPI_CP_BASE = IIAPI_CP_CHAR_WIDTH
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3128
try:
    IIAPI_CP_TOP = IIAPI_CP_DATE_ALIAS
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3341
try:
    IIAPI_XA_JOIN = 2097152
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3386
try:
    IIAPI_XA_FAIL = 536870912
except:
    pass

# /home/ingres/IngresII/ingres/files/iiapi.h: 3466
try:
    IIAPI_XA_1PC = 1073741824
except:
    pass

_IIAPI_DATAVALUE = struct__IIAPI_DATAVALUE # /home/ingres/IngresII/ingres/files/iiapi.h: 734

_IIAPI_DESCRIPTOR = struct__IIAPI_DESCRIPTOR # /home/ingres/IngresII/ingres/files/iiapi.h: 813

_IIAPI_FDATADESCR = struct__IIAPI_FDATADESCR # /home/ingres/IngresII/ingres/files/iiapi.h: 909

_IIAPI_COPYMAP = struct__IIAPI_COPYMAP # /home/ingres/IngresII/ingres/files/iiapi.h: 965

_IIAPI_SVR_ERRINFO = struct__IIAPI_SVR_ERRINFO # /home/ingres/IngresII/ingres/files/iiapi.h: 1017

_IIAPI_II_TRAN_ID = struct__IIAPI_II_TRAN_ID # /home/ingres/IngresII/ingres/files/iiapi.h: 1041

_IIAPI_II_DIS_TRAN_ID = struct__IIAPI_II_DIS_TRAN_ID # /home/ingres/IngresII/ingres/files/iiapi.h: 1068

_IIAPI_XA_TRAN_ID = struct__IIAPI_XA_TRAN_ID # /home/ingres/IngresII/ingres/files/iiapi.h: 1102

_IIAPI_XA_DIS_TRAN_ID = struct__IIAPI_XA_DIS_TRAN_ID # /home/ingres/IngresII/ingres/files/iiapi.h: 1132

_IIAPI_TRAN_ID = struct__IIAPI_TRAN_ID # /home/ingres/IngresII/ingres/files/iiapi.h: 1170

_IIAPI_GENPARM = struct__IIAPI_GENPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1227

_IIAPI_ABORTPARM = struct__IIAPI_ABORTPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1260

_IIAPI_AUTOPARM = struct__IIAPI_AUTOPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1299

_IIAPI_CANCELPARM = struct__IIAPI_CANCELPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1330

_IIAPI_CATCHEVENTPARM = struct__IIAPI_CATCHEVENTPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1400

_IIAPI_CLOSEPARM = struct__IIAPI_CLOSEPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1432

_IIAPI_COMMITPARM = struct__IIAPI_COMMITPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1465

_IIAPI_CONNPARM = struct__IIAPI_CONNPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1553

_IIAPI_CONVERTPARM = struct__IIAPI_CONVERTPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1598

_IIAPI_FORMATPARM = struct__IIAPI_FORMATPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1647

_IIAPI_DISCONNPARM = struct__IIAPI_DISCONNPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1679

_IIAPI_GETCOLINFOPARM = struct__IIAPI_GETCOLINFOPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1730

_IIAPI_GETCOLPARM = struct__IIAPI_GETCOLPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1783

_IIAPI_GETCOPYMAPPARM = struct__IIAPI_GETCOPYMAPPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1822

_IIAPI_GETDESCRPARM = struct__IIAPI_GETDESCRPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1864

_IIAPI_GETEINFOPARM = struct__IIAPI_GETEINFOPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1926

_IIAPI_GETEVENTPARM = struct__IIAPI_GETEVENTPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 1962

_IIAPI_GETQINFOPARM = struct__IIAPI_GETQINFOPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2102

_IIAPI_INITPARM = struct__IIAPI_INITPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2159

_IIAPI_MODCONNPARM = struct__IIAPI_MODCONNPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2192

_IIAPI_POSPARM = struct__IIAPI_POSPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2238

_IIAPI_PREPCMTPARM = struct__IIAPI_PREPCMTPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2270

_IIAPI_PUTCOLPARM = struct__IIAPI_PUTCOLPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2312

_IIAPI_PUTPARMPARM = struct__IIAPI_PUTPARMPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2353

_IIAPI_QUERYPARM = struct__IIAPI_QUERYPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2421

_IIAPI_REGXIDPARM = struct__IIAPI_REGXIDPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2456

_IIAPI_RELXIDPARM = struct__IIAPI_RELXIDPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2492

_IIAPI_RELENVPARM = struct__IIAPI_RELENVPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2524

_IIAPI_ROLLBACKPARM = struct__IIAPI_ROLLBACKPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2559

_IIAPI_SAVEPTPARM = struct__IIAPI_SAVEPTPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2601

_IIAPI_SCROLLPARM = struct__IIAPI_SCROLLPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2650

_IIAPI_SETENVPRMPARM = struct__IIAPI_SETENVPRMPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2694

_IIAPI_PROMPTPARM = struct__IIAPI_PROMPTPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2895

_IIAPI_TRACEPARM = struct__IIAPI_TRACEPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2935

_IIAPI_EVENTPARM = struct__IIAPI_EVENTPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 2978

_IIAPI_SETCONPRMPARM = struct__IIAPI_SETCONPRMPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 3027

_IIAPI_SETDESCRPARM = struct__IIAPI_SETDESCRPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 3240

_IIAPI_TERMPARM = struct__IIAPI_TERMPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 3268

_IIAPI_WAITPARM = struct__IIAPI_WAITPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 3300

_IIAPI_XASTARTPARM = struct__IIAPI_XASTARTPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 3347

_IIAPI_XAENDPARM = struct__IIAPI_XAENDPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 3388

_IIAPI_XAPREPPARM = struct__IIAPI_XAPREPPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 3427

_IIAPI_XACOMMITPARM = struct__IIAPI_XACOMMITPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 3468

_IIAPI_XAROLLPARM = struct__IIAPI_XAROLLPARM # /home/ingres/IngresII/ingres/files/iiapi.h: 3507

# No inserted files

