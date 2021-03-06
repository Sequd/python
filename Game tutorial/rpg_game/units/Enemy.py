from units.Unit import *


class Enemy(Unit):
    def __init__(self, screen, file_name, x, y, d, name, hp, mp):
        Unit.__init__(self, screen, file_name, x, y, d, name, hp, mp)
        self.speed *= 0.5
        self.is_render_ui = True

    def AI(self):
        if self.moving[LEFT] == 1:
            self.set_direction(LEFT)
            if self.position[X] <= 0 + 200:
                self.moving[LEFT] = 0
                self.moving[RIGHT] = 1

        if self.moving[RIGHT] == 1:
            self.set_direction(RIGHT)
            if self.position[X] >= SCREEN_WIDTH - HERO_SPRITE_WIDTH - 200:
                self.moving[RIGHT] = 0
                self.moving[LEFT] = 1

        if self.moving == [0, 0, 0, 0]:
            self.moving[LEFT] = 1

    def update(self):
        self.AI()
        Unit.update(self)


class Skeleton(Enemy):
    def __init__(self, screen, x=300, y=300):
        Enemy.__init__(self, screen, './data/skeleton.png', x, y, DOWN, 'Skeleton', 100, 0)
