from tkinter import *
# создаём окно приложения и холст
root=Tk()
root.title('Дуга и сектор')
canvas=Canvas(root,width=250,height=170,bg='white')
canvas.pack()
# рисуем описанный прямоугольник
rect=canvas.create_rectangle(30,20,230,150)
# рисуем дугу и сектор
arc = canvas.create_arc(30,20,230,150,
                        start=40,extent=270,
                        width=21,outline='yellow',style='arc')
pie = canvas.create_arc(30,20,230,150,
                        start=40,extent=270,
                        width=3,outline='red')
root.mainloop()