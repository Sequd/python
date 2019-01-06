import math
import turtle

windows = turtle.Screen()
windows.setup(1200 + 3, 800 + 3)
windows.bgcolor('#3d3b47')
windows.screensize(1200, 800)

# Начальные координаты базы
BASE_X, BASE_Y = 0, -300
missiles = []


def fire_missale(x, y):
    """Конструируем и стреляем ракету"""
    global missile
    missile = turtle.Turtle()
    missile.hideturtle()
    missile.speed(0)
    missile.color('white')
    missile.penup()
    missile.setpos(x=BASE_X, y=BASE_Y)
    missile.pendown()
    alpha = calc_alpha(x1=BASE_X, y1=BASE_Y, x2=x, y2=y)
    missile.setheading(alpha)
    missile.showturtle()
    # missile.forward(500)
    # missile.shape('circle')
    # missile.shapesize(2)
    # missile.shapesize(3)
    # missile.shapesize(4)
    # missile.shapesize(5)
    # missile.clear()
    # missile.hideturtle()

    info = {'m': missile, 't': [x, y], 's': 'launch', 'r': 0}
    missiles.append(info)


def calc_alpha(x1, y1, x2, y2):
    dx = (x2 - x1)
    dy = (y2 - y1)
    length = (dx ** 2 + dy ** 2) ** .5
    cos_alpha = dx / length
    alpha = math.acos(cos_alpha)
    alpha = math.degrees(alpha)
    return alpha


windows.onclick(fire_missale)

# windows.mainloop()

while True:
    windows.update()

    for info in missiles:
        missile = info['m']
        state = info['s']

        if state == 'launch':
            missile.forward(4)
            target = info['t']
            if missile.distance(x=target[0], y=target[1]) <= 20:
                info['s'] = 'explode'
                missile.shape('circle')
        elif state == 'explode':
            radius = info['r'] + 1
            missile.shapesize(radius)
            info['r'] = radius
            if radius > 5:
                missiles.remove(info)
                missile.clear()
                missile.hideturtle()
