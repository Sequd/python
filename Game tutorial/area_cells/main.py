# main.py
from tkinter import *

from extensions.callinfo import info

# глобальные переменные
# настройки окна
WIDTH = 400
HEIGHT = 400
CELL_SIZE = 20


@info
def click(event):
    if c.find_withtag(CURRENT):
        ids = c.find_withtag(CURRENT)[0]
        c.itemconfig(CURRENT, fill="green")
    # if ids in mines:
    #     c.itemconfig(CURRENT, fill="red")
    # elif ids not in clicked:
    #     clearance(ids)
    #     c.itemconfig(CURRENT, fill="green")
    c.update()


root = Tk()  # Основное окно программы
root.title("Игра")
# область анимации
c = Canvas(root, width=WIDTH, height=HEIGHT, background="white")
c.bind("<Button-1>", click)
for i in range(0, int(WIDTH / CELL_SIZE)):
    for j in range(0, int(WIDTH / CELL_SIZE)):
        # c.create_line(i * CELL_SIZE, 0, i * CELL_SIZE, HEIGHT, fill="black")  # x1, y1, x2, y2
        # c.create_line(0, j * CELL_SIZE, WIDTH, j * CELL_SIZE, fill="black")  # x1, y1, x2, y2
        c.create_rectangle(i * CELL_SIZE, j * CELL_SIZE,
                           i * CELL_SIZE + CELL_SIZE,
                           j * CELL_SIZE + CELL_SIZE, fill='gray')
c.pack()


@info
def add(x, y):
    return x + y


add(1, 2)

# запускаем работу окна
root.mainloop()
