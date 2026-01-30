import functools, time


def zeit_messen(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f'Ausführung von {func.__name__} hat {time.time() - start:2f}s gedauert.')
        return result

    return wrapper


def debug(func):
    @zeit_messen
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        signatur = ", ".join(args_repr + kwargs_repr)
        print(f"Rufe '{func.__name__}({signatur})' auf")
        result = func(*args, **kwargs)
        print(f"{func.__name__}() hat {repr(result)} zurückgeliefert")
        return result

    return wrapper_debug


def verlangsamen_3sec(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time.sleep(3)
        return func(*args, **kwargs)

    return wrapper


@debug
@verlangsamen_3sec
def potenz(basis: float, exponent: float) -> float:
    return basis ** exponent


print(potenz(3, 4))