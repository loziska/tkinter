from tkinter import *
from geom_sys import *
root=Tk()
root.title('Узор розовый')
canvas=Canvas(root, width=200, height=200, bg='white')
canvas.pack()
# задаём параметры рисунка
n=13; R1=30; R2=90
df=360/n; rd=pi*df/180
SC = 2*R1*R2*cos(rd/2)/(R1+R2)
# задаём начало координат
S = (100,100)
V = [(R1,90),(SC,90-df/2),(R2,90),(SC,90+df/2)]
for i in range(n):
    pts = ps2ds(S,V)
    canvas.create_polygon(pts,outline='black',fill='violet')
    V = [(R,fi+df) for (R,fi) in V]
root.mainloop()
