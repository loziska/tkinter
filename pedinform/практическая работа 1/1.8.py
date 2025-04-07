from tkinter import *
# создаём окно приложения и холст
root=Tk()
root.title('Сегменты и сектор')
canvas=Canvas(root, width=250, height=170, bg='white')
canvas.pack()
# рисуем описанный прямоугольник
rect=canvas.create_rectangle(30,20,230,150)
# рисуем два сегмента и сектор
seg1 = canvas.create_arc(30,20,230,150,
                        start=40,extent=140,
                        fill='blue',style='chord')
seg2 = canvas.create_arc(30,20,230,150,
                        start=180,extent=140,
                        fill='blue',style='chord')
pie = canvas.create_arc(30,20,230,150,
                        start=320,extent=80,fill='red')
root.mainloop()