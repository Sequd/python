class Item:
    name = ''

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Planner:
    items = []

    def __add__(self, other):
        self.items.append(other)

    def append(self, item):
        self.items.append(item)

    def __str__(self):
        s = ''
        for i in self.items:
            s = s + i.name
        ss = [i.name for i in self.items]
        return s


item1 = Item("first task")
print(item1)

planner = Planner()

planner.append(item1)

print(planner)
