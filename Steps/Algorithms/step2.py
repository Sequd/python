# Задания 2 степа


# Первое задание
# input 3, output 2
def fib11(n):
    a = [0, 1]
    for i in range(n - 1):
        x = a[i] + a[i + 1]
        a.append(x)
    return a[n]


def fib12(n):
    prev, last = 0, 1
    for i in range(n):
        prev, last = last, prev + last
    return last


def fib13(n):
    prev, last = 0, 1
    i = 1
    while i < n:
        prev, last = last, prev + last
        i += 1
    return last


# Второе задание
# input 875577, output 2
def fib21(n):
    prev, last = 0, 1
    i = 1
    while i < n:
        prev, last = last, (prev + last) % 10
        i += 1
    return last


# Второе задание
# input 10 2, output 1
def fib22(n, m):
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


def fib23(n, m):
    a = [0, 1]
    for i in range(2, m * 6):
        last = (a[i - 1] + a[i - 2]) % m
        a.append(last)
    period = len(a)
    print(a)
    print(period)
    v = n % period
    print(v)
    print(a[v])
    return a[v]


'''
    n, m = map(int, input().split())
    print(fib(n, m))
'''
r = fib23(10, 2)
print(r)
