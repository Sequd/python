import numpy as np
import random

print("Work with matrix :")
a = np.array([[1, 2, 3], [4, 5, 6]])  # создаём массив
print(a)  # смотрим на массив
print(a.shape)  # смотрим на форму массива
print(a[0:2])

print("Flat matrix:")
print(a.flatten())

w = np.array(random.sample(range(100), 12))  # одномерный массив из 12 случайных чисел от 1 до 1000
w = w.reshape((2, 2, 3))  # превратим w в трёхмерную матрицу
print("Test matrix:")
print(w)
print("Transpose:")
print(w.transpose(0, 2, 1))

k = np.eye(3, k=1)  #
print(k)

zero = np.zeros([3, 2])  # массив 3 на 2 с нулями
print(zero)

ones = np.ones([3, 2])  # массив 3 на 2 с единицами
print(ones)

a2 = np.ndarray((3, 4))
print(a2)

buffer = np.array([
    [2, 1, 0, 0],
    [0, 2, 1, 0],
    [0, 0, 2, 1],
    [0, 0, 0, 2]])

a3 = np.ndarray((3, 4), buffer=buffer, dtype=int)
print(a3)

print("вдоль столбцов")
print(a3.mean(axis=0))  # вдоль столбцов

print("вдоль строк")
print(a3.mean(axis=1))  # вдоль строк

print("вдоль всего массива")
print(a3.mean(axis=None))  # вдоль всего массива

print("сумма")
print(a.sum(axis=None))

print("произведение всех элементов вдоль указанной оси")
print(a.prod(axis=None))

print("частичные суммы")
print(a.cumsum(axis=None))

print("произведения вектор частичных сумм")
print(a.cumprod(axis=None))

print("Линейная алгебра:")
a4 = w.dot([1, 2, 3])
print(a)
ainv = np.linalg.inv(a4)
print(a4.dot(ainv))

print("Dictionary:")

words = {}
words["Milk"] = 1
words["Eegs"] = 2
print(words)
pairs = words.items()
sorted(pairs, key=lambda x: x[1], reverse=True)
# pairs.sort(key=lambda x: x[1], reverse=True)
print(pairs)
for p in pairs:  # печатаем первые 10 элементов списка
    print(p[0], p[1])
