from geom_sys import *
from tkinter import *

root=Tk()
root.title('Калейдоскоп')
canvas=Canvas(root,width=200, height=200,bg='white')
canvas.pack()

A=(55,178)
B=(145,178)
C=(100,100)
L1=[(88,130),(100,160),(124,142),(112,130)]
L2=[(70,172),(100,166),(88,142)]
L3=[(105,142),(135,142),(123,172)]
P=C; Q=B; R=A

for k in range(6):
    canvas.create_polygon(P,Q,R,fill='greenyellow',
    width=1,outline='black')
    canvas.create_polygon(L1,fill='purple')
    canvas.create_polygon(L2,fill='blue')
    canvas.create_polygon(L3,fill='magenta')
    R=symmetry(P,Q,R)
    L1=symmetry(P,Q,L1)
    L2=symmetry(P,Q,L2)
    L3=symmetry(P,Q,L3)
    Q,R=R,Q

root.mainloop()
