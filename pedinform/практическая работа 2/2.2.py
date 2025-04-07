from tkinter import *
root=Tk()
root.title('Мишень')
canvas=Canvas(root,width=200,height=200,bg='white')
canvas.pack()
# --------- параметры ---------
(xs,ys)=(100,100); R=90; dR=-20
# -----------------------------
for r in range(R,0,dR):
    canvas.create_oval(xs-r, ys-r, xs+r, ys+r,
                       width=10, outline='blue')   
root.mainloop()