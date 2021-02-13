import random

from core.effects.pixel import Pixel


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


