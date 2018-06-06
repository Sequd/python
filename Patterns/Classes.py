class Unit:
    name = ""

    def __init__(self, name=None):
        if name is not None:
            self.name = name

    def __str__(self):
        return "Unit name is %s" % self.name


class Enemy(Unit):
    def __init__(self, name):
        super().__init__(name)

    def attack(self):
        s = "%s attack" % self.name
        print(s)


class Npc(Unit):
    def __init__(self, name):
        super().__init__(name)

    def give_quest(self):
        s = "NPC %s give you quest" % self.name
        print(s)


# Using classes
unit = Unit()
print(unit)
#
# enemy = Enemy("bad hungry wolf")
# print(enemy)
# enemy.attack()
