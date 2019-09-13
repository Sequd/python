# -*- coding: utf-8 -*-
import numpy
import pygame

from Constants import *

width = 12
height = 12
margin = 1
width_count = (SCREEN_WIDTH // (width + margin))
height_count = (SCREEN_HEIGHT // (height + margin))


def quit_game():
    print("Quit event")
    quit()


class Main:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.enemies = []
        self.gen_current = numpy.random.randint(low=2, size=(width_count, height_count))
        self.gen_next = numpy.zeros((width_count, height_count))

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # Действие при нажатии кнопки
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

    def update(self):

        for row in range(width_count - 1):
            for column in range(height_count - 1):
                column1 = 0 if column + 1 > height_count else column + 1
                row1 = 0 if row + 1 > width_count else row + 1
                a1 = self.gen_current[row - 1][column - 1]
                a2 = self.gen_current[row - 1][column]
                a3 = self.gen_current[row - 1][column1]

                a4 = self.gen_current[row][column - 1]
                a5 = self.gen_current[row][column + 1]

                a6 = self.gen_current[row1][column - 1]
                a7 = self.gen_current[row1][column]
                a8 = self.gen_current[row1][column1]
                s = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8
                if 2 < s < 4:
                    self.gen_next[row][column] = 1
                else:
                    self.gen_next[row][column] = 0

        res = self.gen_current.sum() == self.gen_next.sum()
        if res:
            self.gen_current = numpy.random.randint(low=2, size=(width_count, height_count))
        else:
            self.gen_current = self.gen_next.copy()

    def render(self):
        self.screen.fill(GREY)
        for row in range(width_count):
            for column in range(height_count):
                rect = [(margin + width) * row + margin,
                        (margin + height) * column + margin,
                        width,
                        height]
                color = GREEN if self.gen_current[row][column] == 1 else WHITE
                pygame.draw.rect(self.screen, color, rect)

        # self.timer.render()
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
pygame.display.set_caption('rpg game')
clock = pygame.time.Clock()
game = Main(screen)
game.main_loop()
