from tkinter import *
root=Tk()
root.title('Штриховка')
canvas=Canvas(root,width=210,height=200,bg='white')
canvas.pack()

def partition(A,B,n):
   (xa,ya)=A
   (xb,yb)=B
   dx=(xb-xa)/n
   dy=(yb-ya)/n
   return [(xa+i*dx, ya+i*dy) for i in range(n+1)]

A=( 30,140)
B=(100, 30)
C=(180,160)
n=10
V1=partition(A,B,n)
V2=partition(B,C,n)
for P,Q in zip(V1,V2):
    canvas.create_line(P,Q)
# вершины
canvas.create_text(A,text='A',anchor='se')
canvas.create_text(B,text='B',anchor='s')
canvas.create_text(C,text='C',anchor='sw')
root.mainloop()