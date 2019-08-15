# Вы принимаете от пользователя последовательность чисел, разделённых запятой.
# Составьте список и кортеж с этими числами.

def split_string(string):
    # ints = map(int, string.split(','))
    res1 = [int(i) for i in string.split(',')]
    res2 = tuple(res1)
    res3 = set(res1)
    return res1, res2, res3


lst, tup, set = split_string('123,234,321,555')
print(lst)
print(tup)
print(set)
