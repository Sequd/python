from skills.Skill import *
from units.Inventory import Inventory


class Player(Unit):
    inventory = Inventory()

    def __init__(self, screen, file_name):
        Unit.__init__(self, screen, file_name, START_X, START_Y, RIGHT, 'Player 1', MAX_HP, MAX_MP)

        self.is_render_ui = True
        self.skills = []
        self.skills.append(MEGA_DAMAGE_SKILL())
        self.skills.append(Heal())

    def used_skill(self, skill_num, target):
        self.is_using_skill = True
        self.skills[skill_num].use(target)
