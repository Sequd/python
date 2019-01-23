from Unit import *


class Player(Unit):
    def __init__(self, screen, file_name):
        Unit.__init__(self, screen, file_name, START_X, START_Y, RIGHT, 'Player 1', MAX_HP, MAX_MP)

        self.image_pack = ['./man_right.jpg', './man_down.jpg', './man_left.jpg', './man_up.jpg', './health_bar.jpg',
                           './health_point.jpg', './mana_bar.jpg', './mana_point.jpg']
        self.images = []

        for image in self.image_pack:
            i = pygame.image.load(image)
            self.images.append(i)

    def render(self):
        Unit.render(self)
        self.render_ui()

    def render_ui(self):
        self.screen.blit(self.images[HEALTH_BAR], (self.position[X] + 7, self.position[Y] + 64))
        d_hp = int(self.hp / HEALTH_BAR_SIZE / HEALTH_POINT_SIZE)
        for i, p in enumerate(range(0, d_hp)):
            self.screen.blit(self.images[HEALTH_POINT],
                             (self.position[X] + 7 + (i * HEALTH_POINT_SIZE), self.position[Y] + 64))

        self.screen.blit(self.images[MP_BAR], (self.position[X] + 7, self.position[Y] + 67))
        d_mp = int(self.mp / MP_BAR_SIZE / MP_POINT_SIZE)
        for i, p in enumerate(range(0, d_mp)):
            self.screen.blit(self.images[MP_POINT], (self.position[X] + 7 + (i * MP_POINT_SIZE), self.position[Y] + 67))
