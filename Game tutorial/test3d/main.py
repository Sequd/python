import pygame
import sys
import math

pygame.init()

display_screen = pygame.display.set_mode((800, 600))
font_style = pygame.font.Font(None, 36)
clock = pygame.time.Clock()


class FpsDisplay:
    def __init__(self, font, pos, color="coral"):
        self.font = font
        self.pos = pos
        self.color = color

    def display(self, screen):
        fps = str(int(clock.get_fps()))
        fps_text = self.font.render(fps, 1, pygame.Color(self.color))
        screen.blit(fps_text, self.pos)


class Button:
    def __init__(self, text, pos, size, color="red"):
        self.text = text
        self.pos = pos
        self.size = size
        self.color = color

    def display(self, screen, font):
        button_surface = pygame.Surface(self.size)
        button_surface.fill(pygame.Color(self.color))
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_width, text_height = text_surface.get_size()
        text_pos = ((self.size[0] - text_width) / 2, (self.size[1] - text_height) / 2)
        button_surface.blit(text_surface, text_pos)  # Position text
        screen.blit(button_surface, self.pos)

    def is_clicked(self, pos):
        x, y = self.pos
        w, h = self.size
        if x <= pos[0] <= x + w and y <= pos[1] <= y + h:
            return True
        return False


class Segment:
    def __init__(self, start_pos, end_pos, width=1, line_color="white", circle_radius=5, circle_color="white"):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.width = width
        self.line_color = line_color
        self.circle_radius = circle_radius
        self.circle_color = circle_color

    def draw(self, screen):
        pygame.draw.line(screen, pygame.Color(self.line_color), self.start_pos, self.end_pos, self.width)
        pygame.draw.circle(screen, pygame.Color(self.circle_color), self.start_pos, self.circle_radius)
        pygame.draw.circle(screen, pygame.Color(self.circle_color), self.end_pos, self.circle_radius)


class Square:
    def __init__(self, top_left, side_length, params, fill_color="gray"):
        x, y = top_left
        self.segments = [
            Segment((x, y), (x + side_length, y), **params),
            Segment((x, y), (x, y + side_length), **params),
            Segment((x + side_length, y), (x + side_length, y + side_length), **params),
            Segment((x, y + side_length), (x + side_length, y + side_length), **params)
        ]
        self.corners = [(x, y), (x + side_length, y), (x + side_length, y + side_length), (x, y + side_length)]
        self.fill_color = fill_color

    def draw(self, screen):
        pygame.draw.polygon(screen, pygame.Color(self.fill_color), self.corners)
        for segment in self.segments:
            segment.draw(screen)


class Grid:
    def __init__(self, cell_size, color="gray"):
        self.cell_size = cell_size
        self.color = color

    def draw(self, screen):
        for x in range(0, screen.get_width(), self.cell_size):
            pygame.draw.line(screen, pygame.Color(self.color), (x, 0), (x, screen.get_height()), 1)
        for y in range(0, screen.get_height(), self.cell_size):
            pygame.draw.line(screen, pygame.Color(self.color), (0, y), (screen.get_width(), y), 1)


class Grid2h5D:
    def __init__(self, color='gray', horizon_color='blue', horizon_y=300, cell_size_bottom=50, cell_size_top=10):
        self.color = pygame.Color(color)
        self.horizon_color = pygame.Color(horizon_color)
        self.horizon_y = horizon_y
        self.cell_size_bottom = cell_size_bottom  # size of the bottom-most line
        self.cell_size_top = cell_size_top  # size of the top-most line (at the horizon)

    # The lerp function computes the linear interpolation between two values a and b by a parameter t
    @staticmethod
    def lerp(start, end, t):
        return start + t * (end - start)

    def draw(self, screen):
        v_point = (screen.get_width() - 200 // 2, self.horizon_y-10)
        #pygame.draw.line(screen, self.horizon_color, (0, self.horizon_y), (screen.get_width(), self.horizon_y), 3)

        for x in range(0, screen.get_width(), 40):
            pygame.draw.line(screen, self.color, (x, screen.get_height()), v_point, 1)

        gap_bottom = self.cell_size_bottom
        gap_top = self.cell_size_top
        total_lines = 18 #((screen.get_height() - self.horizon_y) // gap_bottom) + 1

        for i in range(total_lines):
            t = i / total_lines
            gap = self.lerp(gap_bottom, gap_top, t)
            y = screen.get_height() - i * gap
            pygame.draw.line(screen, self.color, (0, y), (screen.get_width(), y), 1)


def game_loop():
    fps_display = FpsDisplay(font_style, (750, 10))
    quit_button = Button('Quit', (0, 0), (100, 50))
    square = Square((300, 300), 200, dict(width=1, line_color="white", circle_radius=5, circle_color="white"),
                    fill_color="gray25")
    grid = Grid(75)
    grid2 = Grid2h5D()  # Создайте объект Grid


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button.is_clicked(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

        display_screen.fill((0, 0, 0))
        # grid.draw(display_screen)
        grid2.draw(display_screen)
        fps_display.display(display_screen)
        quit_button.display(display_screen, font_style)
        square.draw(display_screen)
        pygame.display.flip()
        clock.tick(60)


game_loop()
