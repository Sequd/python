import numpy as np
import matplotlib.pyplot as plt

'''
    Этот скрипт создает и визуализирует векторное поле.
    Использованы библиотеки numpy и matplotlib.
    Массивы x и y создаются с помощью numpy.arange().
    На основе x и y создается сетка координат с помощью numpy.meshgrid().
    Генерируются случайные направления векторов, вычисляемые через косинус и синус.
    Векторы визуализируются с помощью matplotlib.pyplot.quiver() и отображаются с помощью matplotlib.pyplot.show().
'''

# Создаем данные для векторов
x = np.arange(-2, 3, 1)
y = np.arange(-2, 3, 1)
X, Y = np.meshgrid(x, y)

# Генерируем случайные направления для векторов
angles = np.random.rand(len(x), len(y)) * 2 * np.pi
U = np.cos(angles)
V = np.sin(angles)

# Визуализируем векторы с помощью plt.quiver()
plt.quiver(X, Y, U, V, scale=20)
plt.show()
