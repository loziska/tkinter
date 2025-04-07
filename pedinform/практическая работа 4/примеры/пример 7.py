from geom_sys import *
from tkinter import *
root=Tk()
root.title('???')
canvas=Canvas(root,width=400,height=400,bg='white')
canvas.pack()
# задаём параметры узора
(xa,ya)=(80,120); # точка выхода лучей
(xs,ys)=(120,120); R=90; # центр и радиус круга
n=36; u0=0; du=360
# рисуем узор
canvas.create_oval(xs-R,ys-R,xs+R,ys+R)
for k in range(n+1):
    fi=u0+k/n*du
    (x,y)=ps2ds((xs,ys),(R,fi))
    canvas.create_line(xa,ya,x,y)

root.mainloop()
