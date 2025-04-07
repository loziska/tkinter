from tkinter import *
root=Tk()
root.title('Флаг России')
canvas=Canvas(root,width=240,height=160,bg='white')
canvas.pack()
# -------- параметры ---------
(xs,ys)=(30,20); d=40; w=4.5*d
# ----------------------------
canvas.create_rectangle(xs,ys,xs+w,ys+d,fill='#ffffff')
ys+=d
canvas.create_rectangle(xs,ys,xs+w,ys+d,fill='#0072ce')
ys+=d
canvas.create_rectangle(xs,ys,xs+w,ys+d,fill='#ef3340')
root.mainloop()