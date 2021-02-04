from skills.Skill import *
from Constants import *


class TextBox:
    def __init__(self, screen, text, x=150, y=50, w=64, h=32, background=BLACK, text_color=WHITE):
        self.text_color = text_color
        self.background = background
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.screen = screen
        self.font = pygame.font.Font(None, 25)
        self.text = self.font.render(text, True, text_color)
        self.alpha = 255

    def set_alpha(self, alpha):
        if self.alpha is not alpha:
            self.alpha = alpha

    def update(self):
        mouse = pygame.mouse.get_pos()
        self.set_alpha(150)
        if self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y:
            self.set_alpha(255)

    def render(self):
        surf = pygame.Surface((self.w, self.h), pygame.SRCALPHA)
        surf.fill(self.background)
        surf.set_alpha(self.alpha)
        self.screen.blit(surf, (self.x, self.y))
        self.screen.blit(self.text, (self.x, self.y))

    def update_text(self, text):
        self.text = self.font.render(text, True, self.text_color)
