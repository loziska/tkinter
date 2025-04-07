from tkinter import *

def create_circle(obj, S, R,**params):
    (xs,ys) = S
    return obj.create_oval(xs-R,ys-R,xs+R,ys+R,params)

root=Tk()
root.title('Симметрия')
canvas=Canvas(root, width=300, height=200, bg='white')
canvas.pack()
(x0,y0)=(150,100); n=6; dR=10
for i in range(n,0,-1):
    R=i*dR
    create_circle(canvas, (x0-R,y0), R, fill='')
    create_circle(canvas, (x0+R,y0), R, fill='')
canvas.create_line(x0,y0-n*dR, x0,y0+n*dR) 

root.mainloop()
