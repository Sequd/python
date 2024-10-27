import matplotlib.pyplot as plt
import numpy as np


class Interpolator:
    @staticmethod
    def lerp(start, end, t):
        return start + t * (end - start)

    @staticmethod
    def nonlinear_interpolation(start, end, t):
        # Используем квадратичную функцию для нелинейного изменения t
        t = t * t
        return Interpolator.lerp(start, end, t)


# Пример использования
start_value = 200
end_value = 0

# Генерация значений параметра интерполяции от 0 до 1
t_values = np.linspace(0, 1, 100)

# Создаем экземпляр класса Interpolator
interpolator = Interpolator()

# Интерполируем значения и сохраняем результаты
linear_results = [interpolator.lerp(start_value, end_value, t) for t in t_values]
nonlinear_results = [interpolator.nonlinear_interpolation(start_value, end_value, t) for t in t_values]

# Отображение результатов
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(t_values, linear_results, label='Линейная интерполяция')
plt.title('Линейная интерполяция')
plt.xlabel('t')
plt.ylabel('Значение')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(t_values, nonlinear_results, label='Нелинейная интерполяция')
plt.title('Нелинейная интерполяция')
plt.xlabel('t')
plt.ylabel('Значение')
plt.legend()

plt.tight_layout()
plt.show()
