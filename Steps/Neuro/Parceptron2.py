import numpy as np

# начальные веса
w = np.array([0, 0, 0], dtype=float)
# начальные данные
data = np.array([[1, 1, 0.3],
                 [1, 0.4, 0.5],
                 [1, 0.7, 0.8]])
# необходимые результаты
# y - вектор ответов
y = np.array([1, 1, 0])


for i, xi in enumerate(data):
    yi = 1 if w.dot(xi) > 0 else 0
    if yi != y[i]:
        if yi == 0:
            w += xi
        elif yi == 1:
            w -= xi

print(w)
