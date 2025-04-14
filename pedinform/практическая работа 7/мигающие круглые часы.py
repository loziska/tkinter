import time
from tkinter import *
import math
import random  # Для смены цвета

def ps2ds(center, polar_coord):
    x0, y0 = center
    r, angle_degrees = polar_coord
    angle_radians = math.radians(angle_degrees)
    x = x0 + r * math.cos(angle_radians)
    y = y0 - r * math.sin(angle_radians) # Инвертируем y для tkinter
    return x, y

# Функция для создания круга
def create_circle(canvas, center, radius, **kwargs):
    x0, y0 = center
    x1, y1 = x0 - radius, y0 - radius
    x2, y2 = x0 + radius, y0 + radius
    return canvas.create_oval(x1, y1, x2, y2, **kwargs)

root=Tk()
root.title('Часы')
canvas=Canvas(root,width=260,height=300,bg='white') # Увеличиваем высоту для даты
canvas.pack()

# параметры-----------
R1= 40 # длина часовой стрелки
R2= 60 # длина минутной стрелки
R3= 70 # радиус внутреннего круга и секундной стрелки
R4= 90 # срединный радиус числовых отметок
R5=110 # внешний радиус часов
#
(xs,ys)=S=(130,130)
create_circle(canvas,S,R5,width=3, outline='black',fill='#ffeeff')
create_circle(canvas,S,R3,outline='',fill='white')
create_circle(canvas,S,7,outline='',fill='blue')  # отметки на циферблате

# Добавляем секундные деления
for i in range(1, 61):
    fi = 90 - 6 * i
    P = ps2ds(S, (R3 * 0.95, fi))  # Немного короче секундные деления
    Q = ps2ds(S, (R3, fi))
    canvas.create_line(P, Q, width=1, fill='gray')  # Светло-серый цвет

hour=0
for i in range(1,61):
    fi=90-6*i
    if i%5==0:
        hour+=1
        P=ps2ds(S,(R1,fi))
        Q=ps2ds(S,(R3,fi))
        T=ps2ds(S,(R4,fi))
        canvas.create_text(T,text=str(hour),font=('Courier New',20,'bold'))
    else:
        P=ps2ds(S,(R2,fi))
        Q=ps2ds(S,(R3,fi))
        canvas.create_line(P,Q)

date_id = canvas.create_text(130, 280, font=('Arial', 12), fill='black') #  Идентификатор для текста с датой

#  Функция для получения случайного цвета
def random_color():
    return '#%02x%02x%02x' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Функция для обновления часов
def update_clock():
    global bg_color
    tm = time.localtime()
    s = tm.tm_sec
    mi = tm.tm_min
    h = tm.tm_hour % 12

    sfi = 6 * s
    mfi = 6 * (mi + s / 60)
    hfi = 30 * (h + mi / 60)

    Ph = ps2ds(S, (R1, 90 - hfi))
    Pm = ps2ds(S, (R2, 90 - mfi))

    #  Плавное движение секундной стрелки:
    Ps = ps2ds(S, (R3, 90 - sfi)) #sfi = 6 * (s + time.monotonic()%1)

    # Обновление даты
    date_str = time.strftime("%d %B %Y", tm)  # Форматируем дату
    canvas.itemconfig(date_id, text=date_str)

    canvas.delete('hand') # удаляем старые стрелки

    idh=canvas.create_line(S,Ph,width=7,fill='blue', tag='hand')
    idm=canvas.create_line(S,Pm,width=3,fill='blue', tag='hand')
    ids=canvas.create_line(S,Ps,width=1,fill='red', tag='hand')


    canvas.update()

    # Смена цвета фона каждую минуту
    if tm.tm_min % 1 == 0 and tm.tm_sec == 0:
      bg_color = random_color()
      canvas.configure(bg=bg_color)

    root.after(20, update_clock) # Обновляем 50 раз в секунду

bg_color = 'white' # Инициализируем цвет фона
update_clock() # Запускаем обновление
root.mainloop()
