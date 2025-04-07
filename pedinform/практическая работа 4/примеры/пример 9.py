from geom_sys import *
from tkinter import *
root=Tk()
root.title('Звезда')
canvas=Canvas(root,width=400,height=400,bg='white')
canvas.pack()

def sector(obj, A, S, R, n, u0, du, cv, w=1):
    (xa,ya)=A; (xs,ys)=S
    obj.create_arc(xs-R,ys-R,xs+R,ys+R,start=u0,extent=du,style=ARC,outline=cv,width=w)
    for k in range(n+1):
        fi=u0+k/n*du
        (x,y)=ps2ds(S,(R,fi))
        obj.create_line(A,(x,y),fill=cv,width=w)

S=(120,120); R=100
m=8; df=180/m; fi=0
for k in range(m):
    A=ps2ds(S,(0.5*R,fi))
    sector(canvas,A,S,R,10,fi-df,2*df,cv='blue')
    fi=fi+2*df

root.mainloop()
