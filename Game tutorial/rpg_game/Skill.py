from Unit import *
from Constants import *


class Skill:
    def __init__(self, mp_cost, timeout, damage):
        self.timeout = timeout
        self.mp_cost = mp_cost
        self.damage = damage
        self.level = 1
        self.modification_value = 0

    def use(self, target):
        pass

    def self_use(self):
        pass


class Damage_Skill(Skill):
    def __init__(self, mp_cost, timeout, damage):
        Skill.__init__(self, mp_cost, timeout, damage)


class MEGA_DAMAGE_SKILL(Damage_Skill):
    def __init__(self):
        Damage_Skill.__init__(self, 25, 0, 50)

    def use(self, target):
        Skill.use(self, target)
        target.lose_hp(self.damage)


class Heal(Skill):
    def __init__(self):
        Skill.__init__(self, 10, 5, 0)
        self.modification_value = 15

    def use(self, target: Unit):
        Skill.use(self, target)
        if target.hp < target.max_hp:
            target.hp += self.modification_value
        if target.hp > target.max_hp:
            target.hp = target.max_hp
