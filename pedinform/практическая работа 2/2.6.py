from tkinter import *
root=Tk()
root.title('Штриховка')
canvas=Canvas(root, width=200, height=200, bg='white')
canvas.pack()

def partition(A,B,n):
   (xa,ya)=A
   (xb,yb)=B
   dx=(xb-xa)/n
   dy=(yb-ya)/n
   return [(xa+i*dx, ya+i*dy) for i in range(n+1)]
# Задаём координаты вершин четырёхугольника
# и отмечаем их на экране буквами A, B, C, D
# ------------ main -----------
A=( 30,140)
B=(100, 30)
C=(180,160)
D=( 60,180)
canvas.create_line(A,B,C,D,A)
n=20
V1=partition(A,B,n)+partition(B,C,n)
V2=partition(A,D,n)+partition(D,C,n)
for P,Q in zip(V1,V2):
    canvas.create_line(P,Q)   
root.mainloop()