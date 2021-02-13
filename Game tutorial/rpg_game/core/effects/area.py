import pygame

import Constants


class Area:
    def __init__(self, screen, x=0, y=0, w=10, h=10):
        self.screen = screen
        self.w = w
        self.h = h
        self.x = x
        self.y = y

    def update(self):
        pass

    def render(self):
        surf = pygame.Surface((self.w, self.h), pygame.SRCALPHA)
        surf.fill(Constants.GREY)
        surf.set_alpha(128)
        self.screen.blit(surf, (self.x, self.y))
