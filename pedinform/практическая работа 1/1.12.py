from tkinter import *
root=Tk()
root.title('Смайлик')
canvas = Canvas(root,width=200,height=200)
canvas.pack()
canvas.create_rectangle(3,3,200,200,
                        fill='pink',stipple='gray50')
canvas.create_oval(20,20,180,180,
                        fill='yellow',width=5,outline='gray')
canvas.create_oval(60,60,80,90,
                        fill='pink')
canvas.create_oval(120,60,140,90,
                        fill='white')
canvas.create_arc(40,40,160,160,
                        start=210,extent=120,style=CHORD,
                        fill='red')
canvas.create_line(105,60,80,120,130,120,width=8)
root.mainloop()