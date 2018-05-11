# 3 задание
# import math


def standart_gcd(a, b):
    # return math.gcd(a, b)
    while b:
        a, b = b, a % b
    return a


# input 18 35, output 1
# input 14159572 63967072, output 4
def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a

    if a > b:
        return gcd(a % b, b)
    elif a < b:
        return gcd(a, b % a)


def nod(a, b):
    if a == b:
        return a
    while a != b:
        if a == 0:
            return b
        elif b == 0:
            return a
        if a > b:
            a, b = a % b, b
        elif a < b:
            a, b = a, b % a


print(standart_gcd(14159572, 63967072))
print(nod(14159572, 63967072))
