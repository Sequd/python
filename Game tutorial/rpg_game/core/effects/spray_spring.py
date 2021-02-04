import pygame
import random

from Constants import *
from core.effects.spray import Spray
from core.effects.spring import Spring


class SpraySpring:
    def __init__(self, screen, x=250, y=250, alive_time=0):
        self.effects = []
        self.effects.append(Spring(screen, x, y))
        self.effects.append(Spray(screen, x, y))
        self.screen = screen

    def update(self):
        self.effects[1].x, self.effects[1].y = self.effects[0].x1, self.effects[0].y1
        for ef in self.effects:
            ef.update()

    def render(self):
        for ef in self.effects:
            ef.render()
