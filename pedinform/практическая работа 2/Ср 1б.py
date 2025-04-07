from tkinter import *
root=Tk()
root.title('Флаг Швейцарии')
canvas=Canvas(root,width=240,height=240,bg='white')
canvas.pack()
# -------- параметры ---------
(xs,ys)=(30,30); d=50; w=d
# ----------------------------
canvas.create_rectangle(xs,ys,xs+160,ys+160,fill='#da291c')

canvas.create_rectangle(xs+65,ys+30,xs+95,ys+130,fill='#ffffff', outline='#ffffff')
canvas.create_rectangle(xs+30,ys+65,xs+130,ys+95,fill='#ffffff', outline='#ffffff')
root.mainloop()
