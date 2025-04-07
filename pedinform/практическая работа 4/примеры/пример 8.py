from geom_sys import *
from tkinter import *
root=Tk()
root.title('Угол')
canvas=Canvas(root,width=400,height=400,bg='white')
canvas.pack()
# задаём параметры разбиения
(xa,ya)=(20,120) # точка выхода лучей
(xs,ys)=(120,120); R=90; # центр и радиус дуги
n=20; u0=-30; du=60
# рисуем узор
canvas.create_arc(xs-R,ys-R,xs+R,ys+R,start=u0,extent=du,style=ARC)
for k in range(n+1):
    fi=u0+k/n*du
    (x,y)=ps2ds((xs,ys),(R,fi))
    canvas.create_line(xa,ya,x,y)

root.mainloop()
