import math
import random

def perlin_noise(x, y, seed=0):
    def noise(x, y, seed):
        return math.sin(math.sqrt(x ** 2 + y ** 2 + seed))

    return noise(x, y, seed)

# Генерация сетки координат с использованием генераторов списков
x_values = range(-3, 4)
y_values = range(-3, 4)

noise_grid = [[perlin_noise(x, y, random.randint(0, 1000)) for y in y_values] for x in x_values]

# Вычисление dx и dy одновременно
curl_noise = []
for i in range(1, len(noise_grid)-1):
    row = []
    for j in range(1, len(noise_grid[0])-1):
        dx = noise_grid[i+1][j] - noise_grid[i-1][j]
        dy = noise_grid[i][j+1] - noise_grid[i][j-1]
        row.append((dx, dy))
    curl_noise.append(row)

# Вывод результатов
for row in curl_noise:
    for dx, dy in row:
        print(f"({dx}, {dy}) ", end="")
    print()

if __name__ == "__main__":
    for row in curl_noise:
        for dx, dy in row:
            print(f"({dx}, {dy}) ", end="")
        print()
