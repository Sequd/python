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
        self.alpha = 255

    def set_alpha(self, alpha):
        if self.alpha is not alpha:
            self.alpha = alpha

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

        self.set_alpha(150)
        if self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y:
            self.set_alpha(255)
            if self.pressed:
                if self.tick >= self.tick_default:
                    self.action()

        self.tick -= self.tick_step
        if self.tick < 0:
            self.tick = self.tick_default
        self.last_state = click

    def render(self):
        surf = pygame.Surface((self.w, self.h), pygame.SRCALPHA)
        surf.fill(GREEN)
        surf.set_alpha(self.alpha)
        self.screen.blit(surf, (self.x, self.y))

        # draw text
        self.screen.blit(self.text, (self.x, self.y))
