from geom_sys import *
from tkinter import *
root=Tk()
root.title('Хвост павлина')
canvas=Canvas(root,width=400,height=400,bg='white')
canvas.pack()
# задаём параметры разбиения
(xs,ys)=(120,160); R=100;
n=16; u1=-20; du=220
# рисуем узор
for k in range(n+1):
    fi=u1+k/n*du
    (x,y)=ps2ds((xs,ys),(R,fi))
    canvas.create_line(xs,ys,x,y)
    canvas.create_oval(x-8,y-8,x+8,y+8,fill='white')


root.mainloop()
