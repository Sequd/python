def build_tree():
    step = 9
    for i in range(1, step + 1, 2):
        arr = [0 for x in range(step)]
        mid = round(step / 2)
        arr[mid] = i

        if i != 1:
            for j in range(1, i + 1):
                a = step - j - 1
                arr[a] = i

        print(arr)


build_tree()
