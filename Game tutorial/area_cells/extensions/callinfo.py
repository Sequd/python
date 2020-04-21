# callinfo.py


def info(func):
    def wrapper(*args, **kwargs):
        params = tuple(zip(func.__code__.co_varnames, args))
        print("call func: {.__name__}".format(func), params)
        rv = func(*args, **kwargs)
        return rv

    return wrapper
