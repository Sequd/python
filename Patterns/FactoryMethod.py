class Car:
    """Base car"""

    def __init__(self, name):
        self.name = name

    def factory(self):
        if self == "sport":
            return Sportcar()
        elif self == "mini":
            return Minicar()
        assert 0, "Not found car type: " + self
        # else:
        #     raise Exception("Not found car type")

    def __str__(self):
        return "It is %s" % self.name


class Sportcar(Car):
    """Sport car"""

    def __init__(self) -> None:
        super().__init__("Sportcar")


class Minicar(Car):
    """Mini car"""

    def __init__(self) -> None:
        super().__init__("Minicar")


car = Car.factory("sport")
print(car)

car = Car.factory("mini")
print(car)

# car = Car.factory("asd")
