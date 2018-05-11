# Задания 2 степа


# Первое задание
# input 3, output 2
def fib1(n):
    a = [0, 1]
    for i in range(n - 1):
        x = a[i] + a[i + 1]
        a.append(x)
    return a[n]


def fib2(n):
    prev, last = 0, 1
    for i in range(n):
        prev, last = last, prev + last
    return last


def fib3(n):
    prev, last = 0, 1
    i = 1
    while i < n:
        prev, last = last, prev + last
        i += 1
    return last


'''
    n, m = map(int, input().split())
    print(fib(n, m))
'''
r = fib3(3)
print(r)
