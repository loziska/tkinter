from tkinter import *

root=Tk()
root.title('Ромбы')
canvas=Canvas(root, width=600, height=200, bg='white')
canvas.pack()

def create_romb(obj, S, a, b, **params):
    (xs,ys) = S
    return obj.create_polygon(xs,ys-a,xs+b,ys,xs,ys+a,xs-b,ys)

(x0,y0)=(50,100)
a = 50
b = 20

for i in range(5):
    create_romb(canvas, (x0,y0), a, b, fill='')
    x0 += 2*b
    a += 5
    b -= 2

a -= 5   
b += 2
x0 -= 2*b

for j in range(5):
    create_romb(canvas, (x0,y0), a, b, fill='')
    x0 += 2*b
    a -= 5
    b += 2

root.mainloop()
