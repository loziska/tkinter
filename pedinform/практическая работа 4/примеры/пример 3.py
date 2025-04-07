from geom_sys import *
from tkinter import *
root=Tk()
root.title('Штрихи')
canvas=Canvas(root,width=400,height=300,bg='white')
canvas.pack()
(sx,sy)=(50,100);

for R in range(10,91,5):
    canvas.create_arc(sx-R,sy-R,sx+R,sy+R,
    start=-45,style='arc')
(sx,sy)=(170,70);

for R in range(10,91,5):
    canvas.create_arc(sx-R,sy-R,sx+R,sy+R,
    start=-R,style='arc')
(sx,sy)=(270,100);

for R in range(10,91,5):
    canvas.create_arc(sx-R,sy-R,sx+R,sy+R,
    start=-R/2,extent=R,style='arc')

root.mainloop()
