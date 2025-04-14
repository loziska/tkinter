from time import sleep
from tkinter import *

# Функция для создания круга, если она не определена в geom_sys
def create_circle(canvas, center, radius, **kwargs):
    return canvas.create_oval(center[0] - radius, center[1] - radius,
                            center[0] + radius, center[1] + radius, **kwargs)

root = Tk()
root.title('Бильярд')
canvas = Canvas(root, width=220, height=200, bg='white')
canvas.pack()

# Задаём параметры стола и шара
x1, y1 = 20, 20
x2, y2 = 200, 180
x, y = 30, 30
R = 10
Vx, Vy = 10, 10

# Создаем стол
canvas.create_rectangle(x1, y1, x2, y2, outline='red')

# Создаем шар
ball = create_circle(canvas, (x, y), R, fill='green')
trajectory_line = None  # Для хранения ID линии траектории

for k in range(121):
    # Проверяем столкновения со стенками
    if x + Vx - R < x1 or x + Vx + R > x2:
        Vx = -Vx
    if y + Vy - R < y1 or y + Vy + R > y2:
        Vy = -Vy
    
    # Новые координаты
    new_x, new_y = x + Vx, y + Vy
    
    # Удаляем предыдущую линию траектории (если есть)
    if trajectory_line:
        canvas.delete(trajectory_line)
    
    # Рисуем новую линию траектории
    trajectory_line = canvas.create_line(x, y, new_x, new_y)
    
    # Перемещаем шар
    canvas.move(ball, Vx, Vy)
    
    # Обновляем текущие координаты центра шара
    x, y = new_x, new_y
    
    canvas.update()
    sleep(0.05)

