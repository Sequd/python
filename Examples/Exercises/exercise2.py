a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
# exercise 1
c = []
for x in a:
    if x in b:
        c.append(x)
print(c)

# exercise 2
print(list(set(a) & set(b)))

# exercise 3
print(list(filter(lambda x: x in b, a)))

# exercise 4
print([x for x in a if x in b])