from tkinter import *
root=Tk()
root.title('Узор')
canvas=Canvas(root, width=200, height=200, bg='white')
canvas.pack()

def inter(A,B,q):
    (xa,ya)=A
    (xb,yb)=B
    return (xa+q*(xb-xa), ya+q*(yb-ya))
L=[(20,20),(180, 20),(180,180),( 20,180)]
q=0.3; n=3
for i in range(n):
   canvas.create_line(L,L[0],fill='blue')
   L=[inter(L[i],L[(i+1)%4],q) for i in range(4)]
root.mainloop()