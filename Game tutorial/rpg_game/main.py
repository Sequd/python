import pygame
from Player import *
from Timer import *
from Enemy import *
from Constants import *


class Arrow:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d


class Main:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load('./background.jpg')
        self.running = True
        self.player = Player(screen, './man.png')
        self.enemy = Skeleton(screen)
        self.enemy.set_position(300, 350, LEFT)
        self.image_arrows = [RIGHT, DOWN, LEFT, UP]
        self.image_arrows[RIGHT] = pygame.image.load('./arrow_right.png')
        self.image_arrows[DOWN] = pygame.image.load('./arrow_down.png')
        self.image_arrows[LEFT] = pygame.image.load('./arrow_left.png')
        self.image_arrows[UP] = pygame.image.load('./arrow_up.png')
        self.arrows = []
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
                    self.player.used_skill(1 - 1, self.enemy)
                if event.key == pygame.K_2:
                    self.player.used_skill(2 - 1, self.player)
                # if event.key == pygame.K_a:
                #     self.player.is_attack = False
                # if event.key == pygame.K_d:
                #     self.player.is_attack_range = False

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

    def render(self):
        self.screen.blit(self.background, (0, 0))
        for arrow in self.arrows:
            self.screen.blit(self.image_arrows[arrow.d], (arrow.x, arrow.y))
        self.player.render()
        self.enemy.render()
        self.timer.render()
        pygame.display.flip()

    def main_loop(self):
        while self.running:
            clock.tick(FPS)
            self.update()
            self.player.update()
            self.enemy.update()
            # self.enemy.update2 = lambda x: x.position[X] + 2 if x.position[X] < 500 else 100
            # self.enemy.position[X] = self.enemy.update2(self.enemy)
            self.timer.update()
            self.render()
            self.handle_event()


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('rpg game')
clock = pygame.time.Clock()
game = Main(screen)
