from tkinter import *
from geom_sys import *

root=Tk()
root.title('Задание 1 а, б, в, г')
canvas=Canvas(root,width=800,height=800,bg='white')
canvas.pack()

def tri_dygi(sx,sy, u0):
    R = 80
    for i in range(4):
        R -= 10
        canvas.create_arc(sx-R,sy-R,sx+R,sy+R,
                            start=u0,extent=180,style='arc')

#А) 
(xs,ys) = 200,200
R = 60
fi = 0
for i in range(8):
    (x,y) = ps2ds((xs,ys),(R,fi)) 

    tri_dygi(x,y, fi-150)
    fi += 360/8

#Б)
(sx,sy) = 500,150
R = 50
canvas.create_arc(sx-R,sy-R,sx+R,sy+R,start=0,extent=270,style='arc')
(sx,sy) = 600,150
canvas.create_arc(sx-R,sy-R,sx+R,sy+R,start=-90,extent=270,style='arc')

(sx,sy) = 500,250
R = 50
canvas.create_arc(sx-R,sy-R,sx+R,sy+R,start=-270,extent=270,style='arc')
(sx,sy) = 600,250
canvas.create_arc(sx-R,sy-R,sx+R,sy+R,start=-180,extent=270,style='arc')

canvas.create_line((500,150),(600,150),width=2)
canvas.create_line((600,150),(600,250),width=2)
canvas.create_line((600,250),(500,250),width=2)
canvas.create_line((500,150),(500,250),width=2)

#В)
R = 100
sx, sy = 150,600
fi = 0
n = 6
for i in range(n):
    canvas.create_arc(sx-R,sy-R,sx+R,sy+R,start=fi,extent=360/(6/2),style='arc')
    sx, sy = ps2ds((sx,sy),(R,fi)) 
    fi += (360/n)

#Г)
R = 30
sx, sy = 600,650
fi = 0
n = 18
for i in range(n):
    canvas.create_arc(sx-5*R,sy-5*R,sx+0.5*R,sy+0.5*R,start=fi,extent=159,style='arc')
    sx, sy = ps2ds((sx,sy),(R-2,fi)) 
    fi += (360/n)


root.mainloop()
