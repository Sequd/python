import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Линия и ее отражение")

white = (255, 255, 255)
black = (0, 0, 0)

angle = 45  # Угол наклона линии

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(white)

    # Рисование линии
    start_point = (width // 4, height // 2)
    line_length = 100
    end_point = (
        start_point[0] + int(line_length * pygame.math.Vector2(1, 0).rotate(angle).x),
        start_point[1] + int(line_length * pygame.math.Vector2(1, 0).rotate(angle).y),
    )

    pygame.draw.line(screen, black, start_point, end_point, 2)

    # Отражение линии по вертикали
    reflected_end_point = (
        start_point[0] + int(line_length * pygame.math.Vector2(1, 0).rotate(angle).x),
        start_point[1] - int(line_length * pygame.math.Vector2(1, 0).rotate(angle).y),
    )

    pygame.draw.line(screen, black, start_point, reflected_end_point, 2)

    # Обновление экрана
    pygame.display.flip()
