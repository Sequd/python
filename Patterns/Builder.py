from Patterns.Classes import Unit


class UnitBuilder:
    __unit = Unit()

    def set_name(self, name):
        self.__unit.name = name

    def inst(self) -> Unit:
        return self.__unit


b = UnitBuilder()
b.set_name("Markus")
u = b.inst()
print(u)
