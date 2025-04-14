from time import *
from math import *
from tkinter import *

root = Tk()
w=250; h=200
canvas = Canvas(root,width=w,height=h,bg='white')
canvas.pack()
x1=10; x2=w-10
y1=10; y2=h-10
canvas.create_rectangle(x1,y1,x2,y2,fill='lightgray')

n=3; R=15
S=[(220,100,-2,-1),(120,150,2,-1),(100,50,0,-3)]
colors=['lightgreen','lightblue','pink']
balls=[]


for i in range(n):
    x,y,Vx,Vy=S[i]
    balls.append(canvas.create_oval(x-R,y-R,x+R,y+R,fill=colors[i]))
canvas.update()
sleep(0.5)
for k in range(1000):
    for i in range(n):
        x,y,Vx,Vy=S[i]
        if x+Vx-R<x1 or x+Vx+R>x2: Vx=-Vx
        if y+Vy-R<y1 or y+Vy+R>y2: Vy=-Vy
        S[i]=(x+Vx,y+Vy,Vx,Vy)
        canvas.move(balls[i],Vx,Vy)
        canvas.update()
        sleep(0.02)
    for i in range(n):
        xi,yi,Vxi,Vyi=S[i]
        for j in range(i+1,n):
            xj,yj,Vxj,Vyj=S[j]
            dist=sqrt((xj-xi)**2+(yj-yi)**2)
            if dist<2*R+1:
                # столкновение!
                dx,dy=(xj-xi,yj-yi)
                # раскладываем вектор скорости i-ого круга
                q=(Vxi*dx+Vyi*dy)/(dx**2+dy**2)
                Lxi,Lyi=(q*dx,q*dy)
                q=(Vxi*dy-Vyi*dx)/(dx**2+dy**2)
                Nxi,Nyi=(q*dy,-q*dx)
                # раскладываем вектор скорости j-ого круга
                q=(Vxj*dx+Vyj*dy)/(dx**2+dy**2)
                Lxj,Lyj=(q*dx,q*dy)
                q=(Vxj*dy-Vyj*dx)/(dx**2+dy**2)
                Nxj,Nyj=(q*dy,-q*dx)
                # вычисляем новые вектора скоростей
                Vxi,Vyi=(Lxj+Nxi, Lyj+Nyi)
                Vxj,Vyj=(Lxi+Nxj, Lyi+Nyj)
                S[i]=(xi+Vxi,yi+Vyi,Vxi,Vyi)
                S[j]=(xj+Vxj,yj+Vyj,Vxj,Vyj)
                canvas.move(balls[i],Vxi,Vyi)
                canvas.move(balls[j],Vxj,Vyj)
