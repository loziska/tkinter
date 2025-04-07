from tkinter import *
root=Tk()
root.title('Праздник')
canvas=Canvas(root,width=200,height=240,bg='#cceecc')
canvas.pack()
def ballon(x,y,size,**kw):
    line=canvas.create_line(x,y,x,y+3*size)
    oval=canvas.create_oval(x-size,y,x+size,
y-4*size,fill='')
    text=canvas.create_text(x,y-2*size,
                text='',fill='black',
                font=('Comic Sans MS',size//2,'bold'))
    if kw.get('fill')!=None:
        canvas.itemconfig(oval,fill=kw['fill'])
    if kw.get('text')!=None:
        canvas.itemconfig(text,text=kw['text'])
    if kw.get('ctext')!=None:
        canvas.itemconfig(text,fill=kw['ctext'])
ballon(50,140,25,fill='red',text='МИР',ctext='white')
ballon(100,130,30,fill='yellow',text='ЗАМАЙ')
ballon(150,150,25,fill='cyan',text='ТРУД',ctext='blue')
root.mainloop()