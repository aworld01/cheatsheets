# coding: utf-8
get_ipython().run_line_magic('run', 'hello.py #to run .py file')
import json
import getpass
import hashlib

def import_pandas_safely():
    try:
        return __import__('pandas')
    except ImportError:
        return False


__pandas = import_pandas_safely()


def is_data_frame(v: str):
    obj = eval(v)
    if  isinstance(obj, __pandas.core.frame.DataFrame) or isinstance(obj, __pandas.core.series.Series):
        return True


def dataframe_columns(var):
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return [[df.name, str(df.dtype)]]
    return list(map(lambda col: [col, str(df[col].dtype)], df.columns))


def dtypes_str(frame):
    return str(eval(frame).dtypes)

def dataframe_hash(var):
    # Return a hash including the column names and number of rows
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return hashlib.sha256(f"{var}-{df.name},{len(df)}".encode('utf-8')).hexdigest()
    return hashlib.sha256(f"{var}-{','.join(df.columns)},{len(df)}".encode('utf-8')).hexdigest()

def get_dataframes():
    if __pandas is None:
        return []
    user = getpass.getuser()
    values = get_ipython().run_line_magic('who_ls', '')
    dataframes = [
        {
            "name": var,
            "type": type(eval(var)).__name__,
            "hash": dataframe_hash(var),
            "cols": dataframe_columns(var),
            "dtypesStr": dtypes_str(var),
        }
        for var in values if is_data_frame(var)
    ]
    result = {"dataframes": dataframes, "user": user}
    return json.dumps(result, ensure_ascii=False)


get_dataframes()
get_ipython().run_line_magic('load', 'hello.py #to load .py file')
import json
import getpass
import hashlib

def import_pandas_safely():
    try:
        return __import__('pandas')
    except ImportError:
        return False


__pandas = import_pandas_safely()


def is_data_frame(v: str):
    obj = eval(v)
    if  isinstance(obj, __pandas.core.frame.DataFrame) or isinstance(obj, __pandas.core.series.Series):
        return True


def dataframe_columns(var):
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return [[df.name, str(df.dtype)]]
    return list(map(lambda col: [col, str(df[col].dtype)], df.columns))


def dtypes_str(frame):
    return str(eval(frame).dtypes)

def dataframe_hash(var):
    # Return a hash including the column names and number of rows
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return hashlib.sha256(f"{var}-{df.name},{len(df)}".encode('utf-8')).hexdigest()
    return hashlib.sha256(f"{var}-{','.join(df.columns)},{len(df)}".encode('utf-8')).hexdigest()

def get_dataframes():
    if __pandas is None:
        return []
    user = getpass.getuser()
    values = get_ipython().run_line_magic('who_ls', '')
    dataframes = [
        {
            "name": var,
            "type": type(eval(var)).__name__,
            "hash": dataframe_hash(var),
            "cols": dataframe_columns(var),
            "dtypesStr": dtypes_str(var),
        }
        for var in values if is_data_frame(var)
    ]
    result = {"dataframes": dataframes, "user": user}
    return json.dumps(result, ensure_ascii=False)


get_dataframes()
get_ipython().run_line_magic('load', 'hello.py')
import json
import getpass
import hashlib

def import_pandas_safely():
    try:
        return __import__('pandas')
    except ImportError:
        return False


__pandas = import_pandas_safely()


def is_data_frame(v: str):
    obj = eval(v)
    if  isinstance(obj, __pandas.core.frame.DataFrame) or isinstance(obj, __pandas.core.series.Series):
        return True


def dataframe_columns(var):
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return [[df.name, str(df.dtype)]]
    return list(map(lambda col: [col, str(df[col].dtype)], df.columns))


def dtypes_str(frame):
    return str(eval(frame).dtypes)

def dataframe_hash(var):
    # Return a hash including the column names and number of rows
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return hashlib.sha256(f"{var}-{df.name},{len(df)}".encode('utf-8')).hexdigest()
    return hashlib.sha256(f"{var}-{','.join(df.columns)},{len(df)}".encode('utf-8')).hexdigest()

def get_dataframes():
    if __pandas is None:
        return []
    user = getpass.getuser()
    values = get_ipython().run_line_magic('who_ls', '')
    dataframes = [
        {
            "name": var,
            "type": type(eval(var)).__name__,
            "hash": dataframe_hash(var),
            "cols": dataframe_columns(var),
            "dtypesStr": dtypes_str(var),
        }
        for var in values if is_data_frame(var)
    ]
    result = {"dataframes": dataframes, "user": user}
    return json.dumps(result, ensure_ascii=False)


get_dataframes()
"""to load .py file"""
get_ipython().run_line_magic('load', 'hello.py')
import json
import getpass
import hashlib

def import_pandas_safely():
    try:
        return __import__('pandas')
    except ImportError:
        return False


__pandas = import_pandas_safely()


def is_data_frame(v: str):
    obj = eval(v)
    if  isinstance(obj, __pandas.core.frame.DataFrame) or isinstance(obj, __pandas.core.series.Series):
        return True


def dataframe_columns(var):
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return [[df.name, str(df.dtype)]]
    return list(map(lambda col: [col, str(df[col].dtype)], df.columns))


def dtypes_str(frame):
    return str(eval(frame).dtypes)

def dataframe_hash(var):
    # Return a hash including the column names and number of rows
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return hashlib.sha256(f"{var}-{df.name},{len(df)}".encode('utf-8')).hexdigest()
    return hashlib.sha256(f"{var}-{','.join(df.columns)},{len(df)}".encode('utf-8')).hexdigest()

def get_dataframes():
    if __pandas is None:
        return []
    user = getpass.getuser()
    values = get_ipython().run_line_magic('who_ls', '')
    dataframes = [
        {
            "name": var,
            "type": type(eval(var)).__name__,
            "hash": dataframe_hash(var),
            "cols": dataframe_columns(var),
            "dtypesStr": dtypes_str(var),
        }
        for var in values if is_data_frame(var)
    ]
    result = {"dataframes": dataframes, "user": user}
    return json.dumps(result, ensure_ascii=False)


get_dataframes()
get_ipython().run_line_magic('load', 'hello.')
import json
import getpass
import hashlib

def import_pandas_safely():
    try:
        return __import__('pandas')
    except ImportError:
        return False


__pandas = import_pandas_safely()


def is_data_frame(v: str):
    obj = eval(v)
    if  isinstance(obj, __pandas.core.frame.DataFrame) or isinstance(obj, __pandas.core.series.Series):
        return True


def dataframe_columns(var):
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return [[df.name, str(df.dtype)]]
    return list(map(lambda col: [col, str(df[col].dtype)], df.columns))


def dtypes_str(frame):
    return str(eval(frame).dtypes)

def dataframe_hash(var):
    # Return a hash including the column names and number of rows
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return hashlib.sha256(f"{var}-{df.name},{len(df)}".encode('utf-8')).hexdigest()
    return hashlib.sha256(f"{var}-{','.join(df.columns)},{len(df)}".encode('utf-8')).hexdigest()

def get_dataframes():
    if __pandas is None:
        return []
    user = getpass.getuser()
    values = get_ipython().run_line_magic('who_ls', '')
    dataframes = [
        {
            "name": var,
            "type": type(eval(var)).__name__,
            "hash": dataframe_hash(var),
            "cols": dataframe_columns(var),
            "dtypesStr": dtypes_str(var),
        }
        for var in values if is_data_frame(var)
    ]
    result = {"dataframes": dataframes, "user": user}
    return json.dumps(result, ensure_ascii=False)


get_dataframes()
get_ipython().run_line_magic('load', 'hello.py')
import json
import getpass
import hashlib

def import_pandas_safely():
    try:
        return __import__('pandas')
    except ImportError:
        return False


__pandas = import_pandas_safely()


def is_data_frame(v: str):
    obj = eval(v)
    if  isinstance(obj, __pandas.core.frame.DataFrame) or isinstance(obj, __pandas.core.series.Series):
        return True


def dataframe_columns(var):
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return [[df.name, str(df.dtype)]]
    return list(map(lambda col: [col, str(df[col].dtype)], df.columns))


def dtypes_str(frame):
    return str(eval(frame).dtypes)

def dataframe_hash(var):
    # Return a hash including the column names and number of rows
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return hashlib.sha256(f"{var}-{df.name},{len(df)}".encode('utf-8')).hexdigest()
    return hashlib.sha256(f"{var}-{','.join(df.columns)},{len(df)}".encode('utf-8')).hexdigest()

def get_dataframes():
    if __pandas is None:
        return []
    user = getpass.getuser()
    values = get_ipython().run_line_magic('who_ls', '')
    dataframes = [
        {
            "name": var,
            "type": type(eval(var)).__name__,
            "hash": dataframe_hash(var),
            "cols": dataframe_columns(var),
            "dtypesStr": dtypes_str(var),
        }
        for var in values if is_data_frame(var)
    ]
    result = {"dataframes": dataframes, "user": user}
    return json.dumps(result, ensure_ascii=False)


get_dataframes()
import json
import getpass
import hashlib

def import_pandas_safely():
    try:
        return __import__('pandas')
    except ImportError:
        return False


__pandas = import_pandas_safely()


def is_data_frame(v: str):
    obj = eval(v)
    if  isinstance(obj, __pandas.core.frame.DataFrame) or isinstance(obj, __pandas.core.series.Series):
        return True


def dataframe_columns(var):
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return [[df.name, str(df.dtype)]]
    return list(map(lambda col: [col, str(df[col].dtype)], df.columns))


def dtypes_str(frame):
    return str(eval(frame).dtypes)

def dataframe_hash(var):
    # Return a hash including the column names and number of rows
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return hashlib.sha256(f"{var}-{df.name},{len(df)}".encode('utf-8')).hexdigest()
    return hashlib.sha256(f"{var}-{','.join(df.columns)},{len(df)}".encode('utf-8')).hexdigest()

def get_dataframes():
    if __pandas is None:
        return []
    user = getpass.getuser()
    values = get_ipython().run_line_magic('who_ls', '')
    dataframes = [
        {
            "name": var,
            "type": type(eval(var)).__name__,
            "hash": dataframe_hash(var),
            "cols": dataframe_columns(var),
            "dtypesStr": dtypes_str(var),
        }
        for var in values if is_data_frame(var)
    ]
    result = {"dataframes": dataframes, "user": user}
    return json.dumps(result, ensure_ascii=False)


get_dataframes()
import json
import getpass
import hashlib

def import_pandas_safely():
    try:
        return __import__('pandas')
    except ImportError:
        return False


__pandas = import_pandas_safely()


def is_data_frame(v: str):
    obj = eval(v)
    if  isinstance(obj, __pandas.core.frame.DataFrame) or isinstance(obj, __pandas.core.series.Series):
        return True


def dataframe_columns(var):
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return [[df.name, str(df.dtype)]]
    return list(map(lambda col: [col, str(df[col].dtype)], df.columns))


def dtypes_str(frame):
    return str(eval(frame).dtypes)

def dataframe_hash(var):
    # Return a hash including the column names and number of rows
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return hashlib.sha256(f"{var}-{df.name},{len(df)}".encode('utf-8')).hexdigest()
    return hashlib.sha256(f"{var}-{','.join(df.columns)},{len(df)}".encode('utf-8')).hexdigest()

def get_dataframes():
    if __pandas is None:
        return []
    user = getpass.getuser()
    values = get_ipython().run_line_magic('who_ls', '')
    dataframes = [
        {
            "name": var,
            "type": type(eval(var)).__name__,
            "hash": dataframe_hash(var),
            "cols": dataframe_columns(var),
            "dtypesStr": dtypes_str(var),
        }
        for var in values if is_data_frame(var)
    ]
    result = {"dataframes": dataframes, "user": user}
    return json.dumps(result, ensure_ascii=False)


get_dataframes()
get_ipython().run_line_magic('run', 'hello.py')
import json
import getpass
import hashlib

def import_pandas_safely():
    try:
        return __import__('pandas')
    except ImportError:
        return False


__pandas = import_pandas_safely()


def is_data_frame(v: str):
    obj = eval(v)
    if  isinstance(obj, __pandas.core.frame.DataFrame) or isinstance(obj, __pandas.core.series.Series):
        return True


def dataframe_columns(var):
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return [[df.name, str(df.dtype)]]
    return list(map(lambda col: [col, str(df[col].dtype)], df.columns))


def dtypes_str(frame):
    return str(eval(frame).dtypes)

def dataframe_hash(var):
    # Return a hash including the column names and number of rows
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return hashlib.sha256(f"{var}-{df.name},{len(df)}".encode('utf-8')).hexdigest()
    return hashlib.sha256(f"{var}-{','.join(df.columns)},{len(df)}".encode('utf-8')).hexdigest()

def get_dataframes():
    if __pandas is None:
        return []
    user = getpass.getuser()
    values = get_ipython().run_line_magic('who_ls', '')
    dataframes = [
        {
            "name": var,
            "type": type(eval(var)).__name__,
            "hash": dataframe_hash(var),
            "cols": dataframe_columns(var),
            "dtypesStr": dtypes_str(var),
        }
        for var in values if is_data_frame(var)
    ]
    result = {"dataframes": dataframes, "user": user}
    return json.dumps(result, ensure_ascii=False)


get_dataframes()
import json
import getpass
import hashlib

def import_pandas_safely():
    try:
        return __import__('pandas')
    except ImportError:
        return False


__pandas = import_pandas_safely()


def is_data_frame(v: str):
    obj = eval(v)
    if  isinstance(obj, __pandas.core.frame.DataFrame) or isinstance(obj, __pandas.core.series.Series):
        return True


def dataframe_columns(var):
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return [[df.name, str(df.dtype)]]
    return list(map(lambda col: [col, str(df[col].dtype)], df.columns))


def dtypes_str(frame):
    return str(eval(frame).dtypes)

def dataframe_hash(var):
    # Return a hash including the column names and number of rows
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return hashlib.sha256(f"{var}-{df.name},{len(df)}".encode('utf-8')).hexdigest()
    return hashlib.sha256(f"{var}-{','.join(df.columns)},{len(df)}".encode('utf-8')).hexdigest()

def get_dataframes():
    if __pandas is None:
        return []
    user = getpass.getuser()
    values = get_ipython().run_line_magic('who_ls', '')
    dataframes = [
        {
            "name": var,
            "type": type(eval(var)).__name__,
            "hash": dataframe_hash(var),
            "cols": dataframe_columns(var),
            "dtypesStr": dtypes_str(var),
        }
        for var in values if is_data_frame(var)
    ]
    result = {"dataframes": dataframes, "user": user}
    return json.dumps(result, ensure_ascii=False)


get_dataframes()
get_ipython().run_line_magic('load', 'hello.py')
import json
import getpass
import hashlib

def import_pandas_safely():
    try:
        return __import__('pandas')
    except ImportError:
        return False


__pandas = import_pandas_safely()


def is_data_frame(v: str):
    obj = eval(v)
    if  isinstance(obj, __pandas.core.frame.DataFrame) or isinstance(obj, __pandas.core.series.Series):
        return True


def dataframe_columns(var):
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return [[df.name, str(df.dtype)]]
    return list(map(lambda col: [col, str(df[col].dtype)], df.columns))


def dtypes_str(frame):
    return str(eval(frame).dtypes)

def dataframe_hash(var):
    # Return a hash including the column names and number of rows
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return hashlib.sha256(f"{var}-{df.name},{len(df)}".encode('utf-8')).hexdigest()
    return hashlib.sha256(f"{var}-{','.join(df.columns)},{len(df)}".encode('utf-8')).hexdigest()

def get_dataframes():
    if __pandas is None:
        return []
    user = getpass.getuser()
    values = get_ipython().run_line_magic('who_ls', '')
    dataframes = [
        {
            "name": var,
            "type": type(eval(var)).__name__,
            "hash": dataframe_hash(var),
            "cols": dataframe_columns(var),
            "dtypesStr": dtypes_str(var),
        }
        for var in values if is_data_frame(var)
    ]
    result = {"dataframes": dataframes, "user": user}
    return json.dumps(result, ensure_ascii=False)


get_dataframes()
import json
import getpass
import hashlib

def import_pandas_safely():
    try:
        return __import__('pandas')
    except ImportError:
        return False


__pandas = import_pandas_safely()


def is_data_frame(v: str):
    obj = eval(v)
    if  isinstance(obj, __pandas.core.frame.DataFrame) or isinstance(obj, __pandas.core.series.Series):
        return True


def dataframe_columns(var):
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return [[df.name, str(df.dtype)]]
    return list(map(lambda col: [col, str(df[col].dtype)], df.columns))


def dtypes_str(frame):
    return str(eval(frame).dtypes)

def dataframe_hash(var):
    # Return a hash including the column names and number of rows
    df = eval(var)
    if isinstance(df, __pandas.core.series.Series):
        return hashlib.sha256(f"{var}-{df.name},{len(df)}".encode('utf-8')).hexdigest()
    return hashlib.sha256(f"{var}-{','.join(df.columns)},{len(df)}".encode('utf-8')).hexdigest()

def get_dataframes():
    if __pandas is None:
        return []
    user = getpass.getuser()
    values = get_ipython().run_line_magic('who_ls', '')
    dataframes = [
        {
            "name": var,
            "type": type(eval(var)).__name__,
            "hash": dataframe_hash(var),
            "cols": dataframe_columns(var),
            "dtypesStr": dtypes_str(var),
        }
        for var in values if is_data_frame(var)
    ]
    result = {"dataframes": dataframes, "user": user}
    return json.dumps(result, ensure_ascii=False)


get_dataframes()
