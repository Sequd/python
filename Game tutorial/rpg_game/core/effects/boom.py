import pygame
import random

from Constants import *


class Boom:
    def __init__(self, screen, x=250, y=250, alive_time=2):
        # [loc, velocity, timer/radius, color]
        self.particles = []
        self.alive_time = alive_time
        self.x = x
        self.y = y
        self.screen = screen

    def update(self):
        self.x, self.y = pygame.mouse.get_pos()
        if self.alive_time >= 0:
            self.particles.append([[self.x, self.y], [random.randint(0, 20) / 10 - 1, random.randint(0, 20) / 10 - 1], 10, (250, 150, 0)])
            self.particles.append([[self.x, self.y], [random.randint(0, 20) / 10 - 1, random.randint(0, 20) / 10 - 1], random.randint(10, 30), (250, 250, 250)])
        for p in self.particles:
            p[0][0] += p[1][0]
            p[0][1] += p[1][1]
            p[2] -= p[2] / 10

        self.particles = [p for p in self.particles if p[2] > 0]

        self.alive_time -= 0.1

        if self.alive_time < -10:
            self.alive_time = 2

    def render(self):
        for p in self.particles:
            pygame.draw.circle(self.screen, p[3], [int(p[0][0]), int(p[0][1])], int(p[2]))
