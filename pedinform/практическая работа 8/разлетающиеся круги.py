from time import sleep
from random import randint
from geom_sys import *
from tkinter import *

root=Tk()
root.title('Взрыв')
canvas=Canvas(root,width=240,height=240,bg='white')
canvas.pack()
S=(120,120)
n=12; df=360/n; q=0.15
SL=[randint(10,120) for k in range(n)]
fi=0; m=20
for i in range(m):
    t=i/m
    for L in SL:
        A=ps2ds(S,(t*L,fi))
        create_circle(canvas,A,t*L*q,fill='#ddaa66')
        fi+=df
    canvas.update()
    sleep(0.1)
