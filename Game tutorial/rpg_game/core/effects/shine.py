import pygame
import random

from Constants import *


class Shine:
    def __init__(self, screen, x=250, y=250, alive_time=0):
        # [loc, velocity, timer/radius, color, color_step]
        self.particles = []
        self.alive_time = alive_time
        self.x = x
        self.y = y
        self.screen = screen
        self.pixels = []
        self.pixels.append(Pixel(self.screen, x, y))
        self.pixels.append(Pixel(self.screen, x + 10, y))
        self.pixels.append(Pixel(self.screen, x, y + 10))
        self.pixels.append(Pixel(self.screen, x + 10, y + 10))

    def update(self):
        for pixel in self.pixels:
            pixel.x += random.randint(-2, 2)
            pixel.y += random.randint(-2, 2)
            pixel.update()

    def render(self):
        for pixel in self.pixels:
            pixel.render()


class Pixel:
    def __init__(self, screen, x=0, y=0, alive_time=0):
        self.screen = screen
        self.w = 4
        self.h = 4
        self.x = x
        self.y = y
        self.alive_time = alive_time

    def update(self):
        pass

    def render(self):
        rect0 = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(self.screen, WHITE, rect0)
        self.screen.blit(self.screen, (0, 0))


