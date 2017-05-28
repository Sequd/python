import collections


def test_function():
    """I print 'Hello, world!'"""
    print("Hello, world!")


help(test_function)


def test1():
    a = input()
    print(a)


# В качестве альтернативного решения можно использовать чтение напрямую из потока ввода программы:
# import sys
# print(sys.stdin.readline())

def test2():
    # a, b = '16\n64'.split()
    # print(int(a) ** int(b))
    a = input()
    b = input()
    print(int(a) ** int(b))


def test3():
    a = input()
    b = input()
    print("{0} and {1} sat in the tree.\n{0} had fallen, B was stolen.\nWhat's remaining in the tree?".format(a, b))


def test4():
    array = 'A D'.split()
    # cnt = collections.Counter()
    # for a in array:
    #     cnt[a] += 1
    print('%.2f' % (array.count('A') / array.__len__()))


def test5():
    array = {1, 2, 3, 4}
    print(2 in array)
    print(2 not in array)


def unique(interable, seen = None):
    seen = set(seen or []) # None, 0, [], {}, все falsy, если приводить к бул
    acc = []
    for item in interable:
        if item not in seen:
            seen.add(item)
            acc.append(item)
    return acc

xs = [1, 1, 2, 3]
print(unique(xs))

if not []:    # отрецание
    print('false')


test4()
