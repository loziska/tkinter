from tkinter import *
root=Tk()
root.title('Бублики')
canvas=Canvas(root,width=400,height=300,bg='pink')
canvas.pack()
(xs,ys)=(50,170) # центр нижнего эллипса
a=6; b=6; d=12 # полуоси эллипса и величина сдвига
q=1.5 # знаменатель прогрессии
while b<100:
    canvas.create_oval(xs-a, ys-b, xs+a, ys+b,fill='gray')
    canvas.create_oval(xs-a/2, ys-b/2, xs+a/2, ys+b/2,)
    xs+=d
    a*=q; b*=q; d*=q
root.mainloop()
