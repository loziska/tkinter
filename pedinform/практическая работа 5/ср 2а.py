from tkinter import *

root=Tk()
root.title('Ромбы')
canvas=Canvas(root, width=600, height=200, bg='white')
canvas.pack()

def create_romb(obj, S, a, b, **params):
    (xs,ys) = S
    return obj.create_polygon(xs,ys-a,xs+b,ys,xs,ys+a,xs-b,ys)

(x0,y0)=(150,100)
a = 50
b = 50

for i in range(3):
    create_romb(canvas, (x0,y0), a, b, fill='')
    x0 += b

create_romb(canvas, (x0,y0), a+10, b+10, fill='')

x0 += b

for j in range(3):
    create_romb(canvas, (x0,y0), a, b, fill='')
    x0 += b

root.mainloop()
