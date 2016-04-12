import numpy as np


def perceptron(xv, wv):
    return int(sum(x * w for x, w in zip(xv, wv)) > 0)


nums1 = [1, 2, 3]
nums2 = [3, 4, 5]


# sum(a1 * b1 for a1, b1 in zip(xv, wv))


def f(xv, wv):
    z = zip(xv, wv)

    for x, y in z:
        print(x)
        print(x, y)


x1 = [1, 1, 0.3]
w1 = [0, 0, 0]

f(x1, w1)


# v1 = perceptron(x1, w1)
#
# print(v1)
