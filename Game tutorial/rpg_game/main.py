import pygame
from Constants import *
from Player import *


class Main():

    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load('./background.jpg')
        self.running = True
        self.player = Player(screen)
        self.main_loop()

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # Действие при нажатии кнопки
            elif event.type == pygame.KEYDOWN:
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

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.player.render()
        pygame.display.flip()
        # pygame.display.update()

    def main_loop(self):
        while self.running:
            # pygame.time.delay(40)
            self.player.move()
            self.render()
            self.handle_event()


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('rpg game')
game = Main(screen)
