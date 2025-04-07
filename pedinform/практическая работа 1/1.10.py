from tkinter import *
# создаём окно приложения и холст
root=Tk()
root.title('Вывод текста')
canvas=Canvas(root, width=250, height=170, bg='white')
canvas.pack()
# выводим текст
text = canvas.create_text(120,80,
                        text='Вывод текстовой строки',
                        fill='blue', width=200, justify='center',
                        font=('Times New Roman', 28, 'bold italic'))
root.mainloop()