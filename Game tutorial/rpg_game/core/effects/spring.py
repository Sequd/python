import pygame
import random
from Constants import *


class Spring:
    def __init__(self, screen, x=250, y=250):
        self.x1 = x
        self.y1 = y
        self.x2, self.y2 = x, y
        self.screen = screen
        self.velocity = (0, 0)

    def update(self):
        self.x2, self.y2 = pygame.mouse.get_pos()
        self.velocity = [(self.x2 - self.x1) / 10, (self.y2 - self.y1) / 10 + 5]

        self.x1 += self.velocity[0]
        self.y1 += self.velocity[1]

    def render(self):
        # dot 1
        pygame.draw.circle(self.screen, (255, 0, 0), [self.x1, self.y1], 4)
        # dot 2
        pygame.draw.circle(self.screen, (255, 255, 255), [self.x2, self.y2], 4)
        # stick
        pygame.draw.line(self.screen, (255, 255, 255), [self.x1, self.y1], [self.x2, self.y2])
