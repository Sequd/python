# Отсортируйте словарь по значению в порядке возрастания и убывания.
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorter_dict = sorted(d.items(), key=lambda x: x[1])
print(sorter_dict)
