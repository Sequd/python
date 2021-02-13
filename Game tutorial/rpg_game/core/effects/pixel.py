import pygame

import Constants


class Pixel:
    def __init__(self, screen, x=0, y=0, alive_time=0):
        self.screen = screen
        self.w = 4
        self.h = 4
        self.x = x
        self.y = y
        self.alive_time = alive_time

    def circle_surf(self, radius, color):
        surf = pygame.Surface((radius * 2, radius * 2))
        pygame.draw.circle(surf, color, (radius, radius), radius)
        surf.set_colorkey((0, 0, 0))
        return surf

    def update(self):
        pass

    def render(self):
        rect0 = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(self.screen, Constants.WHITE, rect0)

        radius = 8
        surf = self.circle_surf(radius, (20, 20, 60))
        self.screen.blit(surf, (self.x - 6, self.y - 6), special_flags=pygame.BLEND_RGB_ADD)

        self.screen.blit(self.screen, (0, 0))
