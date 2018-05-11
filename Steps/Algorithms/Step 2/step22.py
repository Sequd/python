# Второе задание


# input 875577, output 2
def fib1(n):
    prev, last = 0, 1
    i = 1
    while i < n:
        prev, last = last, (prev + last) % 10
        i += 1
    return last


# input 10 2, output 1
def fib2(n, m):
    prev, last = 0, 1
    a = [0, 1]
    for __ in range(2, n + 1):
        prev, last = last, (prev + last) % m
        a.append(last)
    c = n % len(a[:-2])
    print(len(a))
    print(c)
    print(a)
    return a[c]


def fib3(n, m):
    a = [0, 1]
    prev, last = 0, 1
    for i in range(2, m * 6):
        _m = (a[i - 1] + a[i - 2]) % m
        prev, last = last, (prev + last) % m
        a.append(_m)
    period = len(a)
    print(a)
    print(period)
    v = n % period
    print(v)
    print(a[v])
    return a[v]


r = fib3(10, 2)
