from tkinter import *
root=Tk()
root.title('Решётка')
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
A=( 30, 80)
B=(180, 30)
C=(160,170)
D=( 60,170)
canvas.create_text(A,text='A', anchor=SE)
canvas.create_text(B,text='B', anchor=SW)
canvas.create_text(C,text='C', anchor=NW)
canvas.create_text(D,text='D', anchor=NE)
n=5
# Разбиваем стороны AB и DC
AB=partition(A,B,n)
DC=partition(D,C,n)
# Соединяем пары точек линиями
for P,Q in zip(AB,DC):
    canvas.create_line(P,Q)
# Разбиваем стороны BC и AD
BC=partition(B,C,n)
AD=partition(A,D,n)
# Соединяем пары точек линиями
for P,Q in zip(BC,AD):
    canvas.create_line(P,Q)
root.mainloop()