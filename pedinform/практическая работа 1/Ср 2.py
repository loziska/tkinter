from tkinter import *
# создаём окно приложения и холст
root=Tk()
root.title('Текст и прямугольник')
canvas=Canvas(root,width=250,height=170,bg='white')
canvas.pack()

r3 = canvas.create_rectangle(20,30,230,120,
                            width=5,outline='black',fill='')
text = canvas.create_text(120,80,
                            text='Ohaio!~',
                            fill='blue', width=100, justify='center',
font=('Courier New', 20, 'bold italic'))
root.mainloop()