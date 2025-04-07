from tkinter import *
# создаём окно приложения и холст
root=Tk()
root.title('Ломаная')
canvas=Canvas(root,width=250,height=170,bg='white')
canvas.pack()
r1=canvas.create_rectangle(20,10,135,160,
                            width=0,fill='lime')
r2=canvas.create_rectangle(135,10,230,160,
                            width=0,fill='yellow')
# рисуем сплайн
spline = canvas.create_line(170,20,200,140,50,30,80,150,
                            width=21,fill='black',smooth=True)
line = canvas.create_line(170,20,200,140,50,30,80,150,
                            width=3,fill='red')
root.mainloop()