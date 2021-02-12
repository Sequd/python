import pygame
import random

from Constants import *


class Marker:
    def __init__(self, screen, x=250, y=250):
        self.screen = screen
        self.x = x
        self.y = y

    def update(self):
        pass

    def render(self):
        surface = pygame.Surface((160, 120), pygame.SRCALPHA)

        shift = 20
        pygame.draw.ellipse(surface, (255, 155, 155), (10, 56, 60, 30))
        pygame.draw.ellipse(surface, (0, 0, 0), (10, 56, 60, 30), 1)
        pygame.draw.ellipse(surface, WHITE, (0 + shift, 40 + shift, 40, 20))
        pygame.draw.polygon(surface, WHITE, [[0 + shift, 10 + shift],
                                             [0 + shift, 50 + shift],
                                             [40 + shift, 50 + shift],
                                             [40 + shift, 10 + shift]])
        pygame.draw.ellipse(surface, (255, 155, 155), (0 + shift, 0 + shift, 40, 20))
        pygame.draw.ellipse(surface, (155, 155, 155), (0 + shift, 0 + shift, 40, 20), 1)
        self.screen.blit(surface, (self.x, self.y))
