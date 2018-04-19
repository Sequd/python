import numpy as np
import sys

sys.stdin = open('1.txt', 'r')

x_shape = tuple(map(int, input().split()))
X = np.fromiter(map(int, input().split()), np.int).reshape(x_shape)
y_shape = tuple(map(int, input().split()))
Y = np.fromiter(map(int, input().split()), np.int).reshape(y_shape)

try:
    c = X.dot(Y.T)
    print(X)
    print(Y)
    print(Y.T)
    print(c)

except ValueError:
    print("matrix shapes do not match")
