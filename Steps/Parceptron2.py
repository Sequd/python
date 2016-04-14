import numpy as np
import random

wv = np.array([0, 0, 0], dtype=float)
full = np.array([[1, 1, 0.3], [1, 0.4, 0.5], [1, 0.7, 0.8]], dtype=float)
res = np.array([1, 1, 0])
index = 0

a = np.array((1, 2), dtype=int)
print(a)
print(a.shape)


def process(step):
    if step > 0:
        return 1
    else:
        return 0


for x in full:
    step1 = process(wv.T.dot(x))
    if step1 != res[index]:
        if step1 == 0:
            wv += x
        elif step1 == 1:
            wv -= x
    index += 1
    print(wv)
