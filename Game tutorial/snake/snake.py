# snake.py

from tkinter import *
from extensions.callinfo import info

# глобальные переменные
# настройки окна
WIDTH = 400
HEIGHT = 400
SNAKE_SPEED = 20
CELL_SIZE = 20


class Snake:
    tail = []
    direction = RIGHT
    direction_dict = {
        LEFT: (-CELL_SIZE, 0),
        TOP: (0, -CELL_SIZE),
        RIGHT: (CELL_SIZE, 0),
        BOTTOM: (0, CELL_SIZE),
    }

    def addTail(self, x, y):
        self.tail.append(rect(x, y))

    def move(self):
        dx, dy = self.direction_dict[self.direction]
        b = canvas.bbox(self.tail[0])
        canvas.move(self.tail[0], dx, dy)
        for t in self.tail:
            pass

    @info
    def eat(self, x, y):
        print("EAT FOOD")
        self.addTail(x, y)


@info
def click(event):
    if canvas.find_withtag(CURRENT):
        ids = canvas.find_withtag(CURRENT)[0]
        canvas.itemconfig(CURRENT, fill="green")
    canvas.update()


@info
# функция обработки нажатия клавиш
def movement_handler(event):
    if event.keysym == "w" or event.keysym == "Up":
        snake.direction = TOP
    elif event.keysym == "s" or event.keysym == "Down":
        snake.direction = BOTTOM
    elif event.keysym == "a" or event.keysym == "Left":
        snake.direction = LEFT
    elif event.keysym == "d" or event.keysym == "Right":
        snake.direction = RIGHT


root = Tk()  # Основное окно программы
root.title("Игра")


def rect(x, y):
    return canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill='white')


# область анимации
canvas = Canvas(root, width=WIDTH, height=HEIGHT, background="white")
canvas.bind("<Button-1>", click)
canvas.bind("<KeyPress>", movement_handler)
for i in range(0, int(WIDTH / CELL_SIZE)):
    for j in range(0, int(WIDTH / CELL_SIZE)):
        canvas.create_rectangle(i * CELL_SIZE, j * CELL_SIZE,
                                i * CELL_SIZE + CELL_SIZE,
                                j * CELL_SIZE + CELL_SIZE, fill='gray')
food = canvas.create_oval(WIDTH / 2 - CELL_SIZE, HEIGHT / 2 - CELL_SIZE, WIDTH / 2, HEIGHT / 2, fill='red')
snake = Snake()
snake.addTail(0, 0)
canvas.focus_set()
canvas.pack()


def main():
    snake.move()
    head = snake.tail[0]
    b = canvas.bbox(head)
    b2 = canvas.bbox(food)
    if b == b2:
        snake.eat(b2[0], b[1])
        canvas.coords(food, 0, 0, 40, 40)
        # canvas.move(food, 0, 0, CELL_SIZE + CELL_SIZE, CELL_SIZE + CELL_SIZE)

    # x1, y1, x2, y2 = canvas.coords(oval)
    # canvas.coords(oval, x1 + 5, y1 + 5, x2 + 5, y2 + 5)
    # вызываем саму себя каждые 30 миллисекунд
    root.after(250, main)


main()
# запускаем работу окна
root.mainloop()
