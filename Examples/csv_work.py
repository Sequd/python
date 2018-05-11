import csv


def read_csv_0():
    # with .. as используется для безопасной работы с контекстом
    # аналог using() в шарпе
    with open('file.csv') as csvDataFile:
        csv_reader = csv.reader(csvDataFile)
        for row in csv_reader:
            print(row)


def read_csv():
    d = []
    s = []

    with open('file.csv') as csvDataFile:
        csv_reader = csv.reader(csvDataFile)
        h = next(csv_reader)  # заголовки
        for row in csv_reader:
            d.append(row[0])
            s.append(row[1])
    return d, s, h


dates, scores, headers = read_csv()

print(headers)
print(dates)
print(scores)


def read_as_column():
    d = []
    s = []
    columns = []

    with open('file.csv') as csvDataFile:
        csv_reader = csv.reader(csvDataFile)
        headers = next(csv_reader)  # заголовки

        for row in csv_reader:
            column = {}
            for i, name in enumerate(headers):
                column[name] = row[i].strip()
            columns.append(column)

    return d, s, headers, columns


a, b, c, columns = read_as_column()

row = columns[1]
print(row)
print("User %s have score %s on %s date" % (row["name"], row["score"], row["date"]))
