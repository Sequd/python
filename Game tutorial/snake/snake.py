# snake.py

from tkinter import *
import time
from extensions.callinfo import info

# глобальные переменные
# настройки окна
WIDTH = 400
HEIGHT = 400
SNAKE_SPEED = 20
CELL_SIZE = 20


@info
def click(event):
    if canvas.find_withtag(CURRENT):
        ids = canvas.find_withtag(CURRENT)[0]
        canvas.itemconfig(CURRENT, fill="green")
    canvas.update()


@info
# функция обработки нажатия клавиш
def movement_handler(event):
    # if event.keysym == "w":
    #     LEFT_PAD_SPEED = -SNAKE_SPEED
    # elif event.keysym == "s":
    #     LEFT_PAD_SPEED = SNAKE_SPEED
    # elif event.keysym == "Up":
    #     RIGHT_PAD_SPEED = -SNAKE_SPEED
    # elif event.keysym == "Down":
    #     RIGHT_PAD_SPEED = SNAKE_SPEED
    pass


root = Tk()  # Основное окно программы
root.title("Игра")

# область анимации
canvas = Canvas(root, width=WIDTH, height=HEIGHT, background="white")
canvas.bind("<Button-1>", click)
canvas.bind("<KeyPress>", movement_handler)
for i in range(0, int(WIDTH / CELL_SIZE)):
    for j in range(0, int(WIDTH / CELL_SIZE)):
        canvas.create_rectangle(i * CELL_SIZE, j * CELL_SIZE,
                                i * CELL_SIZE + CELL_SIZE,
                                j * CELL_SIZE + CELL_SIZE, fill='gray')
oval = canvas.create_oval(10, 10, 40, 40, fill='white')
canvas.focus_set()
canvas.pack()


def main():
    canvas.move(oval, 5, 0)

    # x1, y1, x2, y2 = canvas.coords(oval)
    # canvas.coords(oval, x1 + 5, y1 + 5, x2 + 5, y2 + 5)
    # вызываем саму себя каждые 30 миллисекунд
    root.after(33, main)


# def tick(fps, callback):
#     frame = 0
#     start = time.perf_counter()
#     while True:
#         callback()
#         frame += 1
#         target = frame / fps
#         passed = time.perf_counter() - start
#         differ = target - passed
#         if differ < 0:
#             raise ValueError('callback was too slow')
#         time.sleep(differ)
#
#
# tick(24, lambda: main())

main()
# запускаем работу окна
root.mainloop()
