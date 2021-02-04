import pygame
import random

from Constants import *


class Spray:
    def __init__(self, screen, x=250, y=250, alive_time=0):
        # [loc, velocity, timer/radius]
        self.particles = []
        self.alive_time = alive_time
        self.x = x
        self.y = y
        self.screen = screen

    def update(self):
        if self.alive_time >= 0:
            # [random.randint(0, 20) / 10 - 1, -3]
            self.particles.append([[self.x, self.y], [random.randint(0, 20) / 10 - 1, random.randint(0, 20) / 10 - 1], random.randint(2, 4)])
        for p in self.particles:
            p[0][0] += p[1][0]
            p[0][1] += p[1][1]
            p[2] -= 0.1
            p[1][1] += 0.1

        self.particles = [p for p in self.particles if p[2] > 0]

        if self.alive_time > 0:
            self.alive_time -= 0.1

    def render(self):
        for p in self.particles:
            pygame.draw.circle(self.screen, (255, 0, 0), [int(p[0][0]), int(p[0][1])], int(p[2]))
