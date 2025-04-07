from geom_sys import *
from tkinter import *

root=Tk()
root.title('Салфетка')
canvas=Canvas(root,width=200, height=200,bg='white')
canvas.pack()

S=(100,100)
n=42; df=360/n
A=ps2ds(S,(90,0))
B=ps2ds(S,(70,df))
V1=[(20,0),(40,df/2),(60,df/2),(40,0)]
V2=[(70,0),(50,df/2),(80,0)]
L1=ps2ds(S,V1)
L2=ps2ds(S,V2)
P=S; Q=B; R=A

for k in range(n):
    canvas.create_polygon(P,Q,R,fill='Indigo')
    canvas.create_polygon(L1,fill='BlueViolet')
    canvas.create_polygon(L2,fill='MediumPurple')
    R=symmetry(P,Q,R)
    L1=symmetry(P,Q,L1)
    L2=symmetry(P,Q,L2)
    Q,R=R,Q

root.mainloop()
