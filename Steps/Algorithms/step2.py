def fibonachi(n):
    a = [0, 1]
    for i in range(n - 1):
        x = a[i] + a[i + 1]
        a.append(x)

    c = len(a) - 1
    return a[c]

r = fibonachi(3)
print(r)
