from Patterns.Classes import *
import abc


class BaseFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create(self):
        pass


class EnemyFactory(BaseFactory):

    def create(self):
        return Enemy("Big food")


class NpcFactory(BaseFactory):
    def create(self):
        return Npc("King under mountain")


unit = EnemyFactory().create()

print(unit)
