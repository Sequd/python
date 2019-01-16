import pygame
from Constants import *


class Player():

    def __init__(self, screen):
        self.screen = screen
        self.direction = RIGHT
        self.state = ALIVE
        self.position = [START_X, START_Y, RIGHT]
        self.name = 'Player 1'
        self.image_pack = ['./man_right.jpg', './man_down.jpg', './man_left.jpg', './man_up.jpg']
        self.images = []
        for image in self.image_pack:
            i = pygame.image.load(image)
            self.images.append(i)
        # load from sets
        # for image in range(0, 4):
        #     temp = pygame.image.load(image).convert_alpha()
        #     i = []
        #     i.append(temp.subsurface(0, 0, 55, 55))
        self.mooving = [0, 0, 0, 0]

    def moov(self):
        pass

    def render(self):
        self.screen.blit(self.images[self.direction], (self.position[X], self.position[Y]))

    def render_ui(self):
        pass
