import functools


def cache(func):
    cached_results = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cached_results:
            return cached_results[key]
        result = func(*args, **kwargs)
        cached_results[key] = result

        return result

    return wrapper


@cache
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(10))

print(factorial(10))
