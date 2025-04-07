from geom_sys import *
from tkinter import *
root=Tk()
root.title('Узорчик')
canvas=Canvas(root,width=200, height=200,bg='white')
canvas.pack()
q=10; n=8; df=360/n
(sx,sy)=S=(100,100)
V=[(1,1),(9,2),(5,4),(9,-2),(1,-1)]
L=[(sx+q*x,sy+q*y) for (x,y) in V]
for i in range(n):
    canvas.create_line(L)
    L=turn(S,L,df)
root.mainloop()
