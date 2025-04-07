from tkinter import *
root=Tk()
root.title('Флаг Франции')
canvas=Canvas(root,width=240,height=160,bg='white')
canvas.pack()
# -------- параметры ---------
(xs,ys)=(30,20); d=50; w=d
# ----------------------------
canvas.create_rectangle(xs,ys,xs+d,ys+100,fill='#000091')
xs+=d
canvas.create_rectangle(xs,ys,xs+d,ys+100,fill='#ffffff')
xs+=d
canvas.create_rectangle(xs,ys,xs+d,ys+100,fill='#E1000F')
root.mainloop()
