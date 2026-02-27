from functools import wraps

def decorator_func(any_func):
    @wraps(any_func)
    def wrapper_func(*args, **kwargs):
        """This is wrapper function doc"""
        print("This is awesome function...")
        return any_func(*args, **kwargs)
    return wrapper_func


@decorator_func
def add(a,b):
    """This is add function..."""
    return a+b

print(add.__doc__)
print(add.__name__)