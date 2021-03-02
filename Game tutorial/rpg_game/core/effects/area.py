import pygame

import Constants


class Area:
    def __init__(self, screen, color, x=0, y=0, w=10, h=10):
        self.screen = screen
        self.color = color
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.alpha = 100

    def rect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)

    def update(self):
        pass

    def render(self):
        surf = pygame.Surface((self.w, self.h), pygame.SRCALPHA)
        surf.fill(self.color)
        surf.set_alpha(self.alpha)
        # pygame.draw.line(self.screen, (0, 0, 0), (self.x, self.y + self.h - 2), (self.x + self.w, self.y + self.h - 2), 2)
        self.screen.blit(surf, (self.x, self.y))
