# -*- coding: utf-8 -*-
from controls.ChangeRange import ChangeRange
from controls.TextBox import TextBox
from core.Marker import Marker
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


class Arrow:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d

    def get_rect(self):
        return pygame.Rect(self.x, self.y, 15, 15)


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
        self.player = Player(screen, './data/man.png')
        self.enemies = []
        self.enemies.append(Skeleton(screen, 400, 400))
        enemy = Skeleton(screen)
        enemy.set_position(300, 350, LEFT)
        self.enemies.append(enemy)

        # resources
        self.background = pygame.image.load('./data/background.jpg')
        self.image_arrows = [RIGHT, DOWN, LEFT, UP]
        self.image_arrows[RIGHT] = pygame.image.load('./data/arrow_right.png')
        self.image_arrows[DOWN] = pygame.image.load('./data/arrow_down.png')
        self.image_arrows[LEFT] = pygame.image.load('./data/arrow_left.png')
        self.image_arrows[UP] = pygame.image.load('./data/arrow_up.png')
        self.arrows = []

        # controls
        self.controls = []
        self.controls.append(Button(screen, "Exit", action=quit_game))
        self.controls.append(TextBox(screen, "Hello world", 250, 50, 120, 32))
        self.controls.append(ChangeRange(screen, 450, 50, 120, 32))

        # effects
        self.effects = []
        self.effects.append(SpraySpring(screen, 250, 250))
        self.effects.append(Boom(screen, 350, 350))
        self.effects.append(Shine(screen, 550, 150))

        self.markers = []
        self.markers.append(Marker(screen, 250, 250))

    def inputs(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

            # Действие при нажатии кнопки
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    pygame.quit()

                if event.key == pygame.K_RIGHT:
                    self.player.position[D] = RIGHT
                    self.player.moving = [1, 0, 0, 0]
                if event.key == pygame.K_DOWN:
                    self.player.position[D] = DOWN
                    self.player.moving = [0, 1, 0, 0]
                if event.key == pygame.K_LEFT:
                    self.player.position[D] = LEFT
                    self.player.moving = [0, 0, 1, 0]
                if event.key == pygame.K_UP:
                    self.player.position[D] = UP
                    self.player.moving = [0, 0, 0, 1]

                if event.key == pygame.K_a:
                    self.player.is_attack = True
                if event.key == pygame.K_d:
                    a = Arrow(
                        x=self.player.position[X] + HERO_SPRITE_HEIGHT / 2,
                        y=self.player.position[Y] + HERO_SPRITE_WIDTH / 2,
                        d=self.player.position[D]
                    )
                    self.arrows.append(a)
                    self.player.is_attack_range = True

            # Действие при отжатии
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.moving[RIGHT] = 0
                if event.key == pygame.K_DOWN:
                    self.player.moving[DOWN] = 0
                if event.key == pygame.K_LEFT:
                    self.player.moving[LEFT] = 0
                if event.key == pygame.K_UP:
                    self.player.moving[UP] = 0

                if event.key == pygame.K_SPACE:
                    self.player.lose_hp(5)

                if event.key == pygame.K_1:
                    self.player.used_skill(1 - 1, self.enemies[0])
                if event.key == pygame.K_2:
                    self.player.used_skill(2 - 1, self.player)

    def handle_event(self):
        self.inputs(pygame.event.get())

    def update(self):

        for arrow in self.arrows:
            if arrow.d == UP:
                arrow.y -= ARROW_SPEED
            if arrow.d == DOWN:
                arrow.y += ARROW_SPEED
            if arrow.d == RIGHT:
                arrow.x += ARROW_SPEED
            if arrow.d == LEFT:
                arrow.x -= ARROW_SPEED

            if arrow.y < 0:
                self.arrows.remove(arrow)
            if arrow.y > SCREEN_HEIGHT - 5:
                self.arrows.remove(arrow)
            if arrow.x < 0:
                self.arrows.remove(arrow)
            if arrow.x > SCREEN_WIDTH - 15:
                self.arrows.remove(arrow)

            gen = (x for x in self.enemies if x.state == ALIVE)
            for enemy in gen:
                if enemy.get_rect().colliderect(arrow.get_rect()):
                    enemy.lose_hp(10)
                    self.arrows.remove(arrow)
                    print("collide")
                    self.effects.append(Spray(screen, arrow.x, arrow.y))

        for control in self.controls:
            control.update()

        for effect in self.effects:
            effect.update()
        for marker in self.markers:
            marker.update()

    def render(self):
        self.screen.blit(self.background, (0, 0))

        for arrow in self.arrows:
            self.screen.blit(self.image_arrows[arrow.d], (arrow.x, arrow.y))

        for enemy in self.enemies:
            enemy.render()

        self.player.render()
        self.timer.render()

        for control in self.controls:
            control.render()

        for effect in self.effects:
            effect.render()

        for marker in self.markers:
            marker.render()

        pygame.display.flip()

    def main_loop(self):
        while self.running:
            clock.tick(FPS)
            self.update()
            for enemy in self.enemies:
                enemy.update()
            self.player.update()
            self.timer.update()
            self.render()
            self.handle_event()


pygame.init()
# pygame.mixer.init()  # pygame module for loading and playing sounds
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption('rpg game')
clock = pygame.time.Clock()
game = Main(screen)
game.main_loop()
