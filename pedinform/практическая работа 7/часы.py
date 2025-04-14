from time import *
from tkinter import *

root = Tk()
root.title('Цифровые часы')
canvas = Canvas(root, width=260, height=80, bg='#aaccff')
canvas.pack()

# Создаем текстовый объект один раз перед циклом
tm = canvas.create_text(130, 40, text='', font=('Courier New', 32, 'bold'))

for k in range(20):
    res = ctime().split()[3]
    # Обновляем текст существующего объекта
    canvas.itemconfig(tm, text=res)
    canvas.update()
    sleep(1)
