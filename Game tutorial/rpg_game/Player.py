import pygame
from Constants import *


class Player():

    def __init__(self, screen):
        self.screen = screen
        self.direction = RIGHT
        self.hp = MAX_HP
        self.mp = MAX_MP
        self.state = ALIVE
        self.position = [START_X, START_Y, RIGHT]
        self.name = 'Player 1'
        self.image_pack = ['./man_right.jpg', './man_down.jpg', './man_left.jpg', './man_up.jpg', './health_bar.jpg',
                           './health_point.jpg', './mana_bar.jpg', './mana_point.jpg']
        self.images = []
        for image in self.image_pack:
            i = pygame.image.load(image)
            self.images.append(i)

        # load from sets
        # for image in range(0, 4):
        #     temp = pygame.image.load(image).convert_alpha()
        #     i = []
        #     i.append(temp.subsurface(0, 0, 55, 55)) # загрузка куска изображения
        self.moving = [0, 0, 0, 0]

    def move(self):
        if self.moving[UP] == 1:
            self.position[Y] -= PLAYER_SPEED
        if self.moving[DOWN] == 1:
            self.position[Y] += PLAYER_SPEED
        if self.moving[RIGHT] == 1:
            self.position[X] += PLAYER_SPEED
        if self.moving[LEFT] == 1:
            self.position[X] -= PLAYER_SPEED

        if self.position[Y] < 0:
            self.position[Y] = 0
        if self.position[Y] > SCREEN_HEIGHT - 55:
            self.position[Y] = SCREEN_HEIGHT - 55
        if self.position[X] < 0:
            self.position[X] = 0
        if self.position[X] > SCREEN_WIDTH - 50:
            self.position[X] = SCREEN_WIDTH - 50

    def lose_hp(self, damage):
        self.hp -= damage

    def render(self):
        self.screen.blit(self.images[self.direction], (self.position[X], self.position[Y]))
        self.render_ui()

    def render_ui(self):
        self.screen.blit(self.images[HEALTH_BAR], (self.position[X], self.position[Y] + 60))
        d_hp = int(self.hp / HEALTH_BAR_SIZE / HEALTH_POINT_SIZE)
        for i, p in enumerate(range(0, d_hp)):
            self.screen.blit(self.images[HEALTH_POINT], (self.position[X] + (i * HEALTH_POINT_SIZE), self.position[Y] + 60))

        self.screen.blit(self.images[MP_BAR], (self.position[X], self.position[Y] + 67))
        d_mp = int(self.mp / MP_BAR_SIZE / MP_POINT_SIZE)
        for i, p in enumerate(range(0, d_mp)):
            self.screen.blit(self.images[MP_POINT], (self.position[X] + (i * MP_POINT_SIZE), self.position[Y] + 67))
