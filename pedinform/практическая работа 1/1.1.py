from tkinter import *
# создаём окно приложения и холст
root=Tk()
root.title('Прямоугольники')
canvas=Canvas(root,width=250,height=170,bg='white')
canvas.pack()
# рисуем три прямоугольника
r1 = canvas.create_rectangle(20,30,200,120,
                            width=0,fill='lime')
r2 = canvas.create_rectangle(120,70,230,140,
                            outline='black',fill='yellow',
                            stipple='gray75')
r3 = canvas.create_rectangle(50,10,170,160,
                            width=5,outline='red',fill='')
root.mainloop()