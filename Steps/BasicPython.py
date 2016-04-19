import collections


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


test4()
