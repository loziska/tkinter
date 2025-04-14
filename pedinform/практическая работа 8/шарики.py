from time import *
from math import *
from tkinter import *

root = Tk()
w=270; h=220
canvas = Canvas(root,width=w,height=h,bg='#aaeeff')
canvas.pack()

n=6; dR=1 # количество кругов и «скорость» их раздувания
S=[(100,160,2),(90,95,2),(50,90,2),
(180,60,2),(120,50,2),(200,140,2)]
colors=['lightgreen','lightblue','pink','cyan','magenta', 'white']
balls=[]
for i in range(n):
    x,y,R=S[i]
    balls.append(canvas.create_oval(x-R,y-R,x+R,y+R,fill=colors[i]))
canvas.update()
sleep(0.5)
for k in range(400):
    for i in range(n):
        x,y,R=S[i]
        canvas.scale(balls[i],x,y,1+dR/R,1+dR/R)


        S[i]=(x,y,R+dR)
        canvas.update()
        sleep(0.05)
    for i in range(n):
        xi,yi,Ri=S[i]
        for j in range(i+1,n):
            xj,yj,Rj=S[j]
            dist=sqrt((xj-xi)**2+(yj-yi)**2)
            if dist<Ri+Rj+1:
                # столкновение!
                canvas.scale(balls[i],xi,yi,2/Ri,2/Ri)
                canvas.scale(balls[j],xj,yj,2/Rj,2/Rj)
                S[i]=(xi,yi,2); S[j]=(xj,yj,2)
                break
