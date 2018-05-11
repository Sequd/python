import random


def init():
    list = [[], [], []]

    for i in range(5):
        for j in list:
            c = random.randint(0, 100)
            j.append(c)

    print(list)

    return list


def find_max1(list):
    max_value = int()
    max_key = int()
    for i, item in enumerate(list):
        a = sum(item)
        if a >= max_value:
            max_value, max_key = a, i
    return max_key, max_value


def find_max2(list):
    return max(sum(i) for i in list)


l = init()
print(find_max1(l))
print((find_max2(l)))
