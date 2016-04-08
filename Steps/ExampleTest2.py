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
