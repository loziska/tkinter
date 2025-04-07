from tkinter import *
root=Tk()
root.title('Треугольники')
canvas=Canvas(root, width=200, height=200, bg='white')
canvas.pack()
def inter(A,B,q):
    (xa,ya)=A
    (xb,yb)=B
    return (xa+q*(xb-xa), ya+q*(yb-ya))
L=[(90,20),(170, 180),(10,170)]
q=0.1; n=15
for i in range(n):
    canvas.create_line(L,L[0],fill='red')
    L=[inter(L[i],L[(i+1)%3],q) for i in range(3)]
root.mainloop()
