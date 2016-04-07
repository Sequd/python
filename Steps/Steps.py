import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])  # создаём массив
print(a)  # смотрим на массив
print(a.shape)  # смотрим на форму массива

k = np.eye(3, k=1)  #
print(k)

zero = np.zeros([3, 2])  # массив 3 на 2 с нулями
print(zero)

ones = np.ones([3, 2])  # массив 3 на 2 с единицами
print(ones)

print(a[0:2])

a2 = np.ndarray((3, 4))
print(a2)

buffer = np.array([
    [2, 1, 0, 0],
    [0, 2, 1, 0],
    [0, 0, 2, 1],
    [0, 0, 0, 2]])

a3 = np.ndarray((3, 4), buffer=buffer, dtype=int)
print(a3)
