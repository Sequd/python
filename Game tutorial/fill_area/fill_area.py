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
from core.SpriteSheet import *
from controls.Button import *
import sys
import random
import numpy


def quit_game():
    print("Quit event")
    # quit()
    sys.exit()


all_x = 18
all_y = 24
dx = 20
dy = 20
area_size = (all_x * dx, all_y * dy)
area_position = (SCREEN_WIDTH / 2 - area_size[0] / 2, SCREEN_HEIGHT / 2 - area_size[1] / 2)


def namestr(obj):
    """Return name of variable from global scope"""
    namespace = globals()
    return [name for name in namespace if namespace[name] is obj]


class Player:
    def __init__(self, name, color):
        self.name = name
        self.score = 0
        self.color = color


class GameProcess:
    def __init__(self, players):
        self.players = players
        self.index = 0
        self.currentPlayer = self.players[self.index]
        self.dice = (0, 0)
        self.roll_the_dice()

    def next_game_step(self):
        """Processed next game step and roll the dice"""
        self.next_current_player()
        return self.roll_the_dice()

    def next_current_player(self):
        """Select next current player"""
        self.index = not self.index
        self.currentPlayer = self.players[self.index]
        # print(self.currentPlayer.name, namestr(self.currentPlayer.color), "Score:", self.currentPlayer.score)

    def roll_the_dice(self):
        a, b = random.randint(1, 6), random.randint(1, 6)
        self.dice = (a, b)
        print("dice:", a, b)
        return a, b

    def set_score(self):
        self.currentPlayer.score += self.dice[0] * self.dice[1]

    def reset(self):
        for c in self.players:
            c.score = 0
        self.index = 0
        self.currentPlayer = self.players[self.index]
        self.roll_the_dice()


class Main:
    def __init__(self, screen):

        # core objects
        self.screen = screen
        self.timer = Timer(screen)

        self.running = True
        self.mouse_pressed = False
        self.max_effects = 0

        # game objects
        players = (Player("player 1", BLUE), Player("player 2", GREEN))
        self.gameProcess = GameProcess(players)
        self.all_areas = []
        self.all_cells = numpy.arange(all_x * all_y)
        self.players_cell = {0: [], 1: []}
        # print(self.players_cell)
        # print(self.all_cells)
        # print(self.all_cells.reshape(all_x, all_y))

        # resources
        # self.background = pygame.image.load('./data/background.jpg')

        # controls
        self.controls = []
        self.controls.append(TextBox(screen, "Заполните поле", SCREEN_WIDTH / 2 - 60, 20, 132, 20))
        self.controls.append(Button(screen, "Exit", action=quit_game, y=50))
        self.controls.append(Button(screen, "Restart", action=self.restart, y=100))
        self.controls.append(TextBox(screen, self.gameProcess.currentPlayer.name, SCREEN_WIDTH / 2 - 60, 40, 132, 20))

        # players score
        self.score_controls = []
        for index, player in enumerate(self.gameProcess.players):
            shift_y = index * 24
            self.controls.append(TextBox(screen, player.name + " :", w=80, h=24, x=50, y=200 + shift_y))
            self.score_controls.append(TextBox(screen, str(player.score), w=64, h=24, x=130, y=200 + shift_y))

        # effects
        self.effects = []
        # self.effects.append(Shine(screen, 550, 150))
        self.set_start_position()

        sprite_sheet = SpriteSheet("dice.png")
        self.dice_frames = []
        x, y = 0, 0  # start position on sprite sheet
        # Load all the right facing images into a list
        for m in range(0, 2):
            x = 0
            for n in range(0, 3):
                image = sprite_sheet.get_image(x, y, 64, 64)
                self.dice_frames.append(image)
                x += 65
            y += 64

        self.dice_image_1 = self.dice_frames[self.gameProcess.dice[0]]
        self.dice_image_2 = self.dice_frames[self.gameProcess.dice[1]]

    def set_start_position(self):

        # todo: refactoring

        # set for player 1
        a, b = self.gameProcess.dice
        cell = (0, 0)
        x, y = area_position[0] + cell[0] * dx, area_position[1] + cell[1] * dy
        area = Area(screen, self.gameProcess.currentPlayer.color, x, y, a * dx, b * dy)
        self.effects.append(area)
        cells = self.rect_to_cells_large(area.rect())
        self.players_cell[self.gameProcess.index] += list(cells)
        self.gameProcess.set_score()
        self.gameProcess.next_game_step()
        self.max_effects += 1

        # set for player 2
        a, b = self.gameProcess.dice
        cell = (all_x - a, all_y - b)
        x, y = area_position[0] + cell[0] * dx, area_position[1] + cell[1] * dy
        area = Area(screen, self.gameProcess.currentPlayer.color, x, y, a * dx, b * dy)
        self.effects.append(area)
        cells = self.rect_to_cells_large(area.rect())
        self.players_cell[self.gameProcess.index] += list(cells)
        self.gameProcess.set_score()
        self.gameProcess.next_game_step()
        self.max_effects += 1

    def rect_to_cells(self, rect: pygame.Rect):
        start_cell = self.get_number_cell((rect.x, rect.y))
        cells = numpy.arange(all_x * all_y).reshape(all_y, all_x)
        c1, r1 = int(start_cell[0]), int(start_cell[1])
        cells = cells[r1:r1 + int(rect.h / dy), c1:c1 + int(rect.w / dx)]
        # print('array:', cells.flatten())
        return cells.flatten()

    def rect_to_cells_large(self, rect: pygame.Rect):
        start_cell = self.get_number_cell((rect.x, rect.y))
        cells = numpy.arange(all_x * all_y).reshape(all_y, all_x)
        c1, r1 = int(start_cell[0]), int(start_cell[1])
        r1, r2 = (r1 - 1, r1 + 1) if r1 - 1 >= 0 else (0, r1 + 1)
        # print("r1, r2", r1, r2)
        # c1 = c1 if c1 - 1 >= 0 else 0
        c1, c2 = (c1 - 1, c1 + 1) if c1 - 1 >= 0 else (0, c1 + 1)
        cells = cells[r1:r2 + int(rect.h / dy), c1:c2 + int(rect.w / dx)]
        # print(r1, r2 + int(rect.h / dy), c1, c1 + int(rect.w / dx) + 1)
        # print(cells)
        # print('large array:', cells.flatten())
        return cells.flatten()

    def restart(self):
        """Reset game state and clean game objects"""
        self.gameProcess.reset()
        self.all_areas = []
        self.players_cell = {0: [], 1: []}
        self.max_effects = 0
        self.effects.clear()

    def inputs(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

            # Действие при нажатии кнопки
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    pygame.quit()

        # mouse processed
        mouse = pygame.mouse.get_pos()
        in_area = area_position[0] < mouse[0] < area_position[0] + area_size[0] \
                  and area_position[1] < mouse[1] < area_position[1] + area_size[1]
        if in_area:
            cell = self.get_number_cell(mouse)
            x, y = area_position[0] + cell[0] * dx, area_position[1] + cell[1] * dy
            if len(self.effects) == self.max_effects:
                a, b = self.gameProcess.dice
                # print('--- add area:', a, b)
                self.effects.append(Area(screen, self.gameProcess.currentPlayer.color, x, y, a * dx, b * dy))

            # click
            click = pygame.mouse.get_pressed(3)

            # todo: refactoring
            if click[0] != self.mouse_pressed:
                self.mouse_pressed = not self.mouse_pressed
                if self.mouse_pressed and self.effects[-1].color != RED:
                    # Click and next step
                    self.effects[-1].alpha = 200
                    # self.all_areas.append(self.effects[-1].rect())
                    cells = self.rect_to_cells_large(self.effects[-1].rect())
                    self.players_cell[self.gameProcess.index] += list(cells)
                    self.gameProcess.set_score()
                    self.gameProcess.next_game_step()
                    self.dice_image_1 = self.dice_frames[self.gameProcess.dice[0] - 1]
                    self.dice_image_2 = self.dice_frames[self.gameProcess.dice[1] - 1]
                    self.controls[3].update_text(self.gameProcess.currentPlayer.name)
                    self.score_controls[self.gameProcess.index].update_text(str(self.gameProcess.currentPlayer.score))
                    self.max_effects += 1

            if not self.mouse_pressed:

                # Move selected place
                self.effects[-1].x = x
                self.effects[-1].y = y
                collise = set(self.players_cell[self.gameProcess.index]) & set(
                    self.rect_to_cells(self.effects[-1].rect()))

                for eff in self.effects[:-1]:
                    if self.effects[-1].rect().colliderect(eff.rect()):
                        self.effects[-1].color = RED
                        break
                    else:
                        self.effects[-1].color = self.gameProcess.currentPlayer.color
                if len(collise) > 0:
                    self.effects[-1].color = self.gameProcess.currentPlayer.color
                    # print(set(self.players_cell[self.gameProcess.index]))
                    # print(set(self.rect_to_cells(self.effects[-1].rect())))
                    # print(len(collise) > 0)
                else:
                    self.effects[-1].color = RED

        elif len(self.effects) > self.max_effects:
            del self.effects[-1]

    def get_number_cell(self, coordinate):
        cell = (numpy.array(coordinate) - numpy.array(area_position)) / numpy.array((dx, dy))
        cell = numpy.floor(cell)
        return cell

    def handle_event(self):
        self.inputs(pygame.event.get())

    def update(self):
        """Update all game elements"""
        self.timer.update()

        for control in self.controls:
            control.update()

        for control in self.score_controls:
            control.update()

        for effect in self.effects:
            effect.update()

    def draw_area(self):
        """ Draw grid and area """
        surf = pygame.Surface((area_size[0] + 1, area_size[1] + 1), pygame.SRCALPHA)
        surf.fill(WHITE)
        surf.set_alpha(200)

        # todo: optimization, rewrite to one circle
        for x in range(all_x + 1):
            x1 = x * dx
            x2 = x * dx
            y1 = 0
            y2 = dy * all_y

            pygame.draw.line(surf, GREY, [x1, y1], [x2, y2])

        for y in range(all_y + 1):
            x1 = 0
            x2 = dx * all_x
            y1 = y * dy
            y2 = y * dy

            pygame.draw.line(surf, GREY, [x1, y1], [x2, y2])
        self.screen.blit(surf, area_position)

    def render(self):
        """Render all game elements"""

        # background
        rect0 = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        pygame.draw.rect(self.screen, GREY, rect0)

        self.draw_area()
        self.timer.render()

        for control in self.controls:
            control.render()

        for control in self.score_controls:
            control.render()

        for effect in self.effects:
            effect.render()

        self.screen.blit(self.dice_image_1, (640, 64))
        self.screen.blit(self.dice_image_2, (640, 64 * 2))

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
