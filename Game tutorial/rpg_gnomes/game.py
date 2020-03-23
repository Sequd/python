# -*- coding: utf-8 -*-
import numpy
import pygame

from Constants import *


def quit_game():
    print("Quit event")
    quit()


class Unit(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface([12, 12])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1

    def update(self):
        self.rect.x += 2 * self.speed
        super().update()


class Gnome(Unit):
    def __init__(self, x, y):
        super().__init__(x, y, BLUE)
        self.speed = 1.2


class Troll(Unit):
    def __init__(self, x, y):
        super().__init__(x, y, RED)
        self.speed = 0.8


class Main:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        # List to hold the sprites
        self.enemies = pygame.sprite.Group()
        self.enemies.add(Troll(150, 300))
        self.gnomes = pygame.sprite.Group()
        self.gnomes.add(Gnome(50, 50))

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # Действие при нажатии кнопки
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

    def update(self):
        # e = self.enemies.sprites()[0]
        # e.rect.x += 1
        self.enemies.update()
        self.gnomes.update()

    def render(self):
        self.screen.fill(GREY)
        self.gnomes.draw(screen)
        self.enemies.draw(screen)
        pygame.display.flip()

    def main_loop(self):
        while self.running:
            clock.tick(FPS)
            self.update()
            self.render()
            self.handle_event()


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('gnomes')
clock = pygame.time.Clock()
game = Main(screen)
game.main_loop()
