from tkinter import *
# создаём окно приложения и холст
root=Tk()
root.title('Скругленный прямоугольник')
canvas=Canvas(root,width=250,height=170,bg='white')
canvas.pack()

# рисуем ломаную
line = canvas.create_line(200,20,30,20,30,160,200,160,200,20,
                        width=6,fill='black')
root.mainloop()