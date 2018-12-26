import turtle
import random

windows = turtle.Screen()
windows.setup(1200 + 3, 800 + 3)
windows.bgcolor('blue')
windows.screensize(1200, 800)

pen = turtle.Turtle()
pen.color('red')


# pen.shape('turtle')

def airplane(y):
    if y < 0:
        pen.color('yellow')
    for x in [-200, 0, 200]:
        pen.penup()
        pen.setpos(x, y)
        pen.pendown()
        pen.circle(random.randint(50, 100))


airplane(100)
airplane(-100)

windows.mainloop()
