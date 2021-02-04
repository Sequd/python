from controls.Button import Button
from controls.TextBox import TextBox
from skills.Skill import *
from Constants import *


class ChangeRange:
    def __init__(self, screen, x=150, y=50, w=64, h=32, step=0.1):
        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.counter = 0.0
        self.step = step

        self.controls = []
        self.controls.append(Button(screen, "down", x=x, y=y, w=32, h=32, action=self.counter_down))
        self.controls.append(TextBox(screen, str(self.counter), x=x + 32, y=y, w=w, h=h))
        self.controls.append(Button(screen, "up", x=x + w + 32, y=y, w=32, h=32, action=self.counter_up))
        self.inner_w = x + w + 32
        self.alpha = 255

    def counter_down(self):
        self.counter -= self.step
        self.counter = round(self.counter, 1)
        self.controls[1].update_text(str(self.counter))

    def counter_up(self):
        self.counter += self.step
        self.counter = round(self.counter, 1)
        self.controls[1].update_text(str(self.counter))

    def set_alpha(self, alpha):
        if self.alpha is not alpha:
            self.alpha = alpha

    def update(self):
        mouse = pygame.mouse.get_pos()
        self.set_alpha(150)
        if self.x + self.inner_w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y:
            self.set_alpha(255)

        for control in self.controls:
            control.set_alpha(self.alpha)
            control.update()

    def render(self):
        for control in self.controls:
            control.render()
