# -*- coding: utf-8 -*-
from controls.ChangeRange import ChangeRange
from controls.TextBox import TextBox
from core.Marker import Marker
from core.effects.area import Area
from core.effects.boom import Boom
from core.effects.shine import Shine
from core.effects.spray_spring import SpraySpring
from core.effects.spring import Spring
from units.Player import *
from core.Timer import *
from core.effects.spray import *
from units.Enemy import *
from controls.Button import *
import sys
import random


def quit_game():
    print("Quit event")
    quit()
    sys.exit()


class Main:
    def __init__(self, screen):

        # core objects
        self.screen = screen
        self.timer = Timer(screen)

        self.running = True

        # game objects
        # self.player = Player(screen, './data/man.png')

        # resources
        # self.background = pygame.image.load('./data/background.jpg')

        # controls
        self.controls = []
        # self.controls.append(Button(screen, "Exit", action=quit_game))
        self.controls.append(TextBox(screen, "Заполните поле", SCREEN_WIDTH / 2 - 60, 20, 132, 20))

        # effects
        self.effects = []
        # self.effects.append(Shine(screen, 550, 150))

    def inputs(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

            # Действие при нажатии кнопки
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    pygame.quit()

        mouse = pygame.mouse.get_pos()
        if 250 < mouse[0] < 550 and 50 < mouse[1] < 550:
            if len(self.effects) == 0:
                print("draw")
                self.effects.append(Area(screen, 150, 150, 250, 250))
        elif len(self.effects) > 0:
            print("clear")
            self.effects.clear()

    def handle_event(self):
        self.inputs(pygame.event.get())

    def update(self):
        self.timer.update()

        for control in self.controls:
            control.update()

        for effect in self.effects:
            effect.update()

    def draw_area(self):
        all_x = 18
        all_y = 24
        dx = 20
        dy = 20
        size = (all_x * dx, all_y * dy)
        size = (size[0] + 1, size[1] + 1)
        surf = pygame.Surface(size, pygame.SRCALPHA)
        surf.fill(WHITE)
        surf.set_alpha(200)

        for x in range(all_x + 1):
            x1 = x * dx
            x2 = x * dx
            y1 = 0
            y2 = dy * all_y

            pygame.draw.line(surf, BLACK, [x1, y1], [x2, y2])

        for y in range(all_y + 1):
            x1 = 0
            x2 = dx * all_x
            y1 = y * dy
            y2 = y * dy

            pygame.draw.line(surf, BLACK, [x1, y1], [x2, y2])
        area_size = (SCREEN_WIDTH / 2 - size[0] / 2, SCREEN_HEIGHT / 2 - size[1] / 2)
        self.screen.blit(surf, area_size)

    def render(self):
        rect0 = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

        pygame.draw.rect(self.screen, GREY, rect0)
        # self.screen.blit(pygame.Rect(), (0, 0))
        self.draw_area()
        self.timer.render()

        for control in self.controls:
            control.render()

        for effect in self.effects:
            effect.render()
        pygame.display.flip()

    def main_loop(self):
        while self.running:
            clock.tick(FPS)
            self.handle_event()
            self.update()
            self.render()


pygame.init()
# pygame.mixer.init()  # pygame module for loading and playing sounds
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption('Game fill area')
clock = pygame.time.Clock()
game = Main(screen)
game.main_loop()
