import numpy as np
import matplotlib.pyplot as plt

# Создаем сетку координат
X = np.linspace(-3, 3, 100)
Y = np.linspace(-3, 3, 100)
x, y = np.meshgrid(X, Y)

# Генерируем шум Perlin
noise = np.random.rand(x.shape[0], y.shape[1])

# Вычисляем CURL шума
dx, dy = np.gradient(noise)

# Визуализируем шум
plt.streamplot(x, y, dx, dy, color=noise, linewidth=2, cmap='viridis')
plt.show()
