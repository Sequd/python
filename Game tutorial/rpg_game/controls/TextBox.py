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

    def update(self):
        pass

    def render(self):
        pygame.draw.rect(self.screen, self.background, [self.x, self.y, self.w, self.h])
        self.screen.blit(self.text, (self.x, self.y))

    def update_text(self, text):
        self.text = self.font.render(text, True, self.text_color)
