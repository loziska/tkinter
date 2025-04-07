from tkinter import *
from geom_sys import *
root=Tk()
root.title('Узор')
canvas=Canvas(root, width=200, height=200, bg='white')
canvas.pack()
# задаём параметры многоугольника
n=13; R1=30; R2=80; df=360/n
# задаём начало координат
S = (100,100)
V = [(R1,90-df),(R2,90),(R1,90+df)]
for i in range(n):
    pts = ps2ds(S,V)
    canvas.create_line(pts)
    V = [(R,fi+df) for (R,fi) in V]
root.mainloop()

