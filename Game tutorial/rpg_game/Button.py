from Unit import *
from Skill import *


class Button:
    def __init__(self, screen, text, x=250, y=250, w=64, h=32, action=None):
        self.action = action
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.screen = screen
        self.font = pygame.font.Font(None, 25)
        self.first_text = self.font.render(text, True, BLACK)

    def handle_events(self):
        pass

    def update(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(click)
        if self.action is not None:
            if self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y:
                if click[0] == 1:
                    self.action()

    def render(self):
        # pygame.draw.rect(self.screen, (216, 169, 3), [self.x, self.y, self.w, self.h])
        # self.screen.blit(self.first_text, [self.x, self.y])
        pass
