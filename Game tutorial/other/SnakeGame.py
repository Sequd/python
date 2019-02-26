import pygame

pygame.init()
win = pygame.display.set_mode((400, 400))
win.fill((30, 40, 50))
pygame.display.set_caption('Snake')

windows_width = 400
windows_height = 400
snake_size = 40
apple_size = 40
snake_body = []
apples = []
# color #9db1cc
x = 50
y = 50
speed = 4

run = True

while run:
    pygame.time.delay(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    if keys[pygame.K_ESCAPE]:
        run = False

    pygame.draw.circle(win, (70, 90, 145), (x, y), 25)
    pygame.display.update()
