import pygame
from SpriteSheet import *
from Constants import *


class Unit:
    def __init__(self, screen, file_name, x, y, d, name, hp, mp):
        self.screen = screen
        self.hp = hp
        self.mp = mp
        self.state = ALIVE
        self.position = [x, y, d]
        self.name = name
        self.file_name = file_name
        self.walking_frames_r = []
        sprite_sheet = SpriteSheet(file_name)

        x, y = 0, 704  # start position on sprite sheet
        # Load all the right facing images into a list
        for n in range(0, 9):
            image = sprite_sheet.get_image(x, y, HERO_SPRITE_WIDTH, HERO_SPRITE_HEIGHT)
            self.walking_frames_r.append(image)
            x += 64

        self.walking_frames_l = []
        x, y = 0, 576
        # Load all the left facing images into a list
        for n in range(0, 9):
            image = sprite_sheet.get_image(x, y, 64, 64)
            self.walking_frames_l.append(image)
            x += 64

        self.walking_frames_up = []
        x, y = 0, 512
        # Load all the left facing images into a list
        for n in range(0, 9):
            image = sprite_sheet.get_image(x, y, 64, 64)
            self.walking_frames_up.append(image)
            x += 64

        self.walking_frames_down = []
        x, y = 0, 640
        # Load all the left facing images into a list
        for n in range(0, 9):
            image = sprite_sheet.get_image(x, y, 64, 64)
            self.walking_frames_down.append(image)
            x += 64

        self.frame = 0
        self.image = self.walking_frames_down[self.frame]
        self.set_direction(d)
        self.moving = [0, 0, 0, 0]

    def set_direction(self, d):
        if d == RIGHT:
            self.image = self.walking_frames_r[self.frame]
        if d == LEFT:
            self.image = self.walking_frames_l[self.frame]
        if d == UP:
            self.image = self.walking_frames_up[self.frame]
        if d == DOWN:
            self.image = self.walking_frames_down[self.frame]

    def set_position(self, x, y, d=RIGHT):
        self.position = [x, y, d]
        self.set_direction(d)

    def update(self):
        if self.moving[RIGHT] == 1:
            self.image = self.walking_frames_r[self.frame]
            if len(self.walking_frames_r) > self.frame + 1:
                self.frame += 1
            else:
                self.frame = 0

        if self.moving[LEFT] == 1:
            self.image = self.walking_frames_l[self.frame]
            if len(self.walking_frames_l) > self.frame + 1:
                self.frame += 1
            else:
                self.frame = 0

        if self.moving[DOWN] == 1:
            self.image = self.walking_frames_down[self.frame]
            if len(self.walking_frames_down) > self.frame + 1:
                self.frame += 1
            else:
                self.frame = 0

        if self.moving[UP] == 1:
            self.image = self.walking_frames_up[self.frame]
            if len(self.walking_frames_up) > self.frame + 1:
                self.frame += 1
            else:
                self.frame = 0

        if self.moving == [0, 0, 0, 0]:
            self.frame = 0

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
        if self.position[Y] > SCREEN_HEIGHT - HERO_SPRITE_HEIGHT:
            self.position[Y] = SCREEN_HEIGHT - HERO_SPRITE_HEIGHT
        if self.position[X] < 0:
            self.position[X] = 0
        if self.position[X] > SCREEN_WIDTH - HERO_SPRITE_WIDTH:
            self.position[X] = SCREEN_WIDTH - HERO_SPRITE_WIDTH

    def lose_hp(self, damage):
        self.hp -= damage

    def render(self):
        self.screen.blit(self.image, (self.position[X], self.position[Y]))
        self.render_rect()

    def render_rect(self):
        if DRAW_RECT:
            pygame.draw.rect(self.screen, GREEN,
                             [self.position[X], self.position[Y], HERO_SPRITE_WIDTH, HERO_SPRITE_HEIGHT], 2)
