"""
можно использовать декоратор
из стандартной либы functools
"""

from functools import lru_cache


def memo(f):
    cache = {}

    def inner(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return inner


def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)


# fib1 = memo(fib1)
fib1 = lru_cache(maxsize=None)(fib1)
print(fib1(80))
