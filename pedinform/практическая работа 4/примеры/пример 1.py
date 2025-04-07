from geom_sys import *
from tkinter import *
root=Tk()
root.title('Цветочек')
canvas=Canvas(root,width=240,height=240,bg='white')
canvas.pack()
R=50; n=6
df=360/n
S=(120,120)
fi=0
for k in range(n):
    (xc,yc)=ps2ds(S,(R,fi))
    canvas.create_oval(xc-R,yc-R,xc+R,yc+R)
    fi=fi+df
    
root.mainloop()
