from skills.Skill import *
from Constants import *


class Button:
    def __init__(self, screen, text, x=150, y=50, w=64, h=32, action=None):
        self.screen = screen

        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.font = pygame.font.Font(None, 25)
        self.text = self.font.render(text, True, BLACK)

        self.action = action
        self.tick_default = self.tick = 5
        self.tick_step = 0.1
        self.pressed = False
        self.last_state = [0, 0, 0]

    def handle_events(self):
        pass

    def update(self):
        if self.action is None:
            return

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(3)

        if click[0] != self.last_state[0]:
            self.pressed = not self.pressed
            self.tick = self.tick_default

        if self.pressed and self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y:
            if self.tick >= self.tick_default:
                self.action()

        self.tick -= self.tick_step
        if self.tick < 0:
            self.tick = self.tick_default
        self.last_state = click

    def render(self):
        pygame.draw.rect(self.screen, GREEN, [self.x, self.y, self.w, self.h])
        self.screen.blit(self.text, (self.x, self.y))
