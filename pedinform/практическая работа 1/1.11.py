from tkinter import *
# создаём окно приложения и холст
root=Tk()
root.title('Шахматы')
canvas=Canvas(root, width=250, height=120, bg='white')
canvas.pack()
# выводим шахматные фигуры
text = canvas.create_text(130,60,
                        text='\u2654\u2655\u2656\u2657\u2658'+
                        '\u2659\u265a\u265b\u265c\u265d\u265e\u265f',
                        fill='blue', width=240, justify='center',
                        font=('Courier New', 28, 'normal'))
root.mainloop()