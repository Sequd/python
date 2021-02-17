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
import numpy


def quit_game():
    print("Quit event")
    quit()
    sys.exit()


all_x = 18
all_y = 24
dx = 20
dy = 20
area_size = (all_x * dx, all_y * dy)
area_position = (SCREEN_WIDTH / 2 - area_size[0] / 2, SCREEN_HEIGHT / 2 - area_size[1] / 2)


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0


class GameProcess:
    def __init__(self, players):
        self.players = players
        self.index = 0
        self.currentPlayer = self.players[self.index]

    def next_game_step(self):
        self.next_player()
        return self.roll_the_dice()

    def next_player(self):
        self.index = not self.index
        self.currentPlayer = self.players[self.index]
        print("Step for", self.currentPlayer.name)

    def roll_the_dice(self):
        a, b = random.randint(1, 6), random.randint(1, 6)
        print("Roll the dice:", a, b)
        return a, b


class Main:
    def __init__(self, screen):

        # core objects
        self.screen = screen
        self.timer = Timer(screen)

        self.running = True

        # game objects
        players = (Player("player 1"), Player("player 2"))
        self.gameProcess = GameProcess(players)

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
        if area_position[0] < mouse[0] < area_position[0] + area_size[0] \
                and area_position[1] < mouse[1] < area_position[1] + area_size[1]:
            if len(self.effects) == 0:
                # print("draw")
                a, b = self.gameProcess.next_game_step()
                # x = int((mouse[0] - area_position[0]) / dx)
                # y = int((mouse[1] - area_position[1]) / dy)
                diff = (numpy.array(mouse) - numpy.array(area_position)) / numpy.array((dx, dy))
                diff = numpy.floor(diff)
                print("diff:", diff)
                # diff2 = (numpy.array(mouse) - numpy.array(area_position))
                # diff2 = numpy.rint(diff2)
                # print("diff2:", numpy.rint(diff2))
                x, y = area_position[0] + diff[0] * dx, area_position[1] + diff[1] * dy
                print("target cell:", x, y)
                self.effects.append(Area(screen, BLUE, x, y, a * dx, b * dy))
        elif len(self.effects) > 0:
            # print("clear")
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
        surf = pygame.Surface((area_size[0] + 1, area_size[1] + 1), pygame.SRCALPHA)
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
        self.screen.blit(surf, area_position)

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
