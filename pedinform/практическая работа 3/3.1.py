from tkinter import *
from geom_sys import *
root=Tk()
root.title('Звезда')
canvas=Canvas(root, width=200, height=200, bg='white')
canvas.pack()
# задаём параметры рисунка
n=5; k=2; R=80
# задаём начало координат
(xs,ys)= S = (100,105)
# задаём полярный угол «нулевой» вершины звезды
fi = 125
# задаём приращение угла
df = 360/n
# вычисляем полярные координаты всех вершин
V = [(R,fi+i*df) for i in range(n)]
# переводим их в экранные координаты
pts = ps2ds(S,V)
# рисуем звездчатый многоугольник
for i in range(n):
    j=(i+k)%n
    canvas.create_line(pts[i],pts[j],width=2)
root.mainloop()
