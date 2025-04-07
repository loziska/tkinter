from tkinter import *
root=Tk()
root.title('Башня')
canvas=Canvas(root,width=200,height=240,bg='white')
canvas.pack()
# ---------------- параметры -------------
(xs,ys)=(100,170) # центр нижнего эллипса
a=90; b=50; d=30  # полуоси эллипса и величина сдвига
q=0.8             # знаменатель прогрессии
# -----------------------------------------
while b>2:
   canvas.create_oval(xs-a, ys-b, xs+a, ys+b,
                      fill='violet')
   ys-=d
   a*=q; b*=q; d*=q
root.mainloop()