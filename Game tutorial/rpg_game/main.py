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
        pass

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.player.render()
        pygame.display.flip()
        # pygame.display.update()

    def main_loop(self):
        while self.running:
            pygame.time.delay(40)
            self.render()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# screen.fill((30, 40, 50))
pygame.display.set_caption('rpg game')
game = Main(screen)
