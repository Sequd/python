# Найдите три ключа с самыми высокими значениями в словаре

d = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
# sorter_dict = sorted(d.items(), key=lambda x: x[1], reverse=True)
sorter_dict = sorted(d, key=d.get, reverse=True)
result = sorter_dict[:3]
print(result)
