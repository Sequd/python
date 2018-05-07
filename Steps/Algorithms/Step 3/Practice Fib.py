# Практика с числами фибоначи
# import rcviz


def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)


cache = {}  # глобальный словарь для кеша


def fib2(n):
    assert n >= 0
    if n not in cache:
        cache[n] = n if n <= 1 else fib2(n - 1) + fib2(n - 2)
    return cache[n]


print(fib2(80))
