import numpy as np
import sys
from urllib.request import urlopen

f = urlopen('https://stepic.org/media/attachments/lesson/16462/boston_houses.csv')
print(f)
data = np.loadtxt(f, usecols=(0, 1, 2, 3), skiprows=1, delimiter=",")
# print(sbux)
# print(sbux[0:4])
print(data.mean(axis=0))
print(data.mean())

x = np.array([[1, 60], [1, 50], [1, 75]])
y = np.array([[10], [7], [12]])
step1 = x.T.dot(x)
step2 = np.linalg.inv(step1)
step3 = step2.dot(x.T)
H = step3.dot(y)

print(H)
