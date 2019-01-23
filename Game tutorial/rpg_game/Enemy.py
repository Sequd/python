from Unit import *


class Enemy(Unit):
    def __init__(self, screen, file_name, x, y, d, name, hp, mp):
        Unit.__init__(self, screen, file_name, x, y, d, name, hp, mp)

    def AI(self):
        pass


class Skeleton(Enemy):
    def __init__(self, screen):
        Enemy.__init__(self, screen, './skeleton.png', 300, 300, DOWN, 'Skeleton', 100, 0)
