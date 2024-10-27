# Создание простой линейной регрессии в чистом Python

# Гиперпараметры
learning_rate = 0.01
epochs = 1000

# Примеры данных для обучения
X_train = [1, 2, 3, 4, 5]
y_train = [2, 4, 6, 8, 10]

# Инициализация весов и смещения
w = 0.0  # Вес
b = 0.0  # Смещение

# Обучение модели
for epoch in range(epochs):
    # Проход по каждому обучающему примеру
    for x, y in zip(X_train, y_train):
        # Предсказание модели
        y_pred = w * x + b

        # Вычисление ошибки
        error = y_pred - y

        # Обновление весов и смещения по градиенту
        w = w - learning_rate * error * x
        b = b - learning_rate * error

# Предсказание для нового значения
X_test = 431
prediction = w * X_test + b
print("Предсказание:", prediction)
print("Ожидаемый:", X_test * 2)
print("Веса:", w, b)