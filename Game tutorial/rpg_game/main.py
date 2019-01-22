import pygame
from Constants import *
from Player import *
from Timer import *


class SpriteSheet(object):
    """ Class used to grab images out of a sprite sheet. """

    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """

        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """

        # Create a new blank image
        image = pygame.Surface([width, height]).convert()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Assuming black works as the transparent color
        image.set_colorkey(constants.BLACK)

        # Return the image
        return image


class Main():

    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load('./background.jpg')
        self.running = True
        self.player = Player(screen, './man.png')
        self.enemy = Player(screen, './skeleton.png')
        self.enemy.set_position(300, 300)
        self.timer = Timer(screen)
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

    def enemy_move(self):
        self.enemy.moving = [0, 0, 1, 0]

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.player.render()
        self.enemy.render()
        self.timer.render()
        pygame.display.flip()
        # pygame.display.update()

    def main_loop(self):
        while self.running:
            # pygame.time.delay(60)
            clock.tick(FPS)
            self.player.move()
            self.player.update()
            self.enemy.move()
            self.enemy.update2 = lambda x: x.position[X] + 2 if x.position[X] < 500 else 100
            self.enemy.position[X] = self.enemy.update2(self.enemy)
            self.timer.update()
            self.render()
            self.handle_event()


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('rpg game')
clock = pygame.time.Clock()
game = Main(screen)
