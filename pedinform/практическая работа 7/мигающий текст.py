from tkinter import *
import time

root = Tk()
root.title("Мигающий текст")

canvas = Canvas(root, width=200, height=100, bg="white")
canvas.pack()

text_id = canvas.create_text(100, 50, text="Мигающий текст", font=("Arial", 20), fill="black")

while True:
    canvas.itemconfig(text_id, state="hidden")  # Скрываем текст
    canvas.update()
    time.sleep(0.5)  # Задержка 0.5 секунды

    canvas.itemconfig(text_id, state="normal")  # Отображаем текст
    canvas.update()
    time.sleep(0.5)  # Задержка 0.5 секунды

root.mainloop()
