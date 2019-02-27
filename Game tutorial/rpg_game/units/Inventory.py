class Inventory:
    coins = 0
    items = []

    def add_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        self.items.remove(item)

    def get_item(self, index):
        return self.items[index]
