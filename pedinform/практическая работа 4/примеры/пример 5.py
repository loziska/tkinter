from geom_sys import *
from tkinter import *
root=Tk()
root.title('Вентилятор')
canvas=Canvas(root,width=400,height=400,bg='white')
canvas.pack()
(sx,sy)=(200,200)
for k in range(3):
    for R in range(10,91,5):
        canvas.create_arc(sx-R,sy-R,sx+R,sy+R, start=k*120-R,style='arc')

root.mainloop()
