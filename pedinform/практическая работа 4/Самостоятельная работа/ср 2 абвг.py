from tkinter import *
from geom_sys import *


def norm_sector(x,y, center_for_dyga, n, u0, R):
    S = (x,y)
    # задаём параметры разбиения

    (xa,ya) = (x,y) # точка выхода лучей
    (xs,ys) = center_for_dyga

    u0=u0-90 #u0 с какого угла начинается дуга у сектора
    #-90 потому что сектора зациклены с верхнего лепестка,
    # 0 это строго направо

    du=180 #du сколько она длится

    # рисуем узор
    canvas.create_arc(xs-R,ys-R,xs+R,ys+R,
                        start=u0,extent=du,style=ARC)

    m = 6; df = 180/m; fi=0
    for k in range(n+1):
        fi = u0 + (k/n)*du
        (x,y) = ps2ds((xs,ys),(R,fi))
        canvas.create_line(xa,ya,x,y)

def sector_for_G(x,y, n, u0, R):
    #u0 с какого угла начинается дуга у сектора
    S = (x,y)
    
    # задаём параметры разбиения
    (xa,ya) = (x,y) # точка выхода лучей
    (xs,ys) = (x,y)

    du=70 #du сколько она длится
    
    # рисуем узор
    canvas.create_arc(xs-R,ys-R,xs+R,ys+R,
                        start=u0,extent=du,style=ARC)

    m = 6; df = 180/m; fi=0
    for k in range(n+1):
        fi = u0 + (k/n)*du
        (x,y) = ps2ds((xs,ys),(R,fi))
        canvas.create_line(xa,ya,x,y)

root=Tk()
root.title('Задание 2 а, б, в, г')
canvas=Canvas(root,width=800,height=800,bg='white')
canvas.pack()

def one(x,y):
    (xs,ys) = (x,y) #центр
    R=100

    n=45; u1=0; du=360

    x_begin, y_begin = xs + R - R/3, ys
    #переменные для центра откуда рисуем линии

    R_inner = R/3 #радиус внутреннего кружка

    # рисуем узор
    for k in range(n+1):
        fi = u1 + (k / n) * du

        (x,y) = ps2ds((xs,ys),(R,fi)) 
        #для расчетов координат шариков остаются начальные x,y
        #вокруг какого центра их рисовать

        x_to_draw, y_to_draw = ps2ds((x_begin,y_begin),(R_inner,fi)) 
        #расчитываем относительно начального центра внутреннего кружка
        #на сколько смещать начало новой линии от этого центра

        canvas.create_line(x_to_draw, y_to_draw, x,y) 

        canvas.create_oval(x-8,y-8,x+8,y+8,fill='white')
        #шарики рисуем как раньше вокруг центра

def two(x,y):
    S=(x,y); R=50
    m=6; df=360/m; fi=0
    for k in range(m):
        A = ps2ds(S,(1.7*R,fi))

        norm_sector(x,y, A, 30, fi, R)

        fi += df

def B(x,y):
    '''центры тоже должны полярно смещаться'''
    S=(x,y); R=50
    m=10; df=360/m; fi=24
    for k in range(m):
        A = ps2ds(S,(1.2*R,fi))
        S = ps2ds((x,y),(10,fi))

        norm_sector(S[0], S[1], A, 20, fi, R)

        fi += df

def G(x,y):
    '''определяем точки откуда выходят лучи'''
    S=(x,y); R=100 #R для дугг
    m=6; df=360/m; fi=0

    fi_for_sector = 110
    R_outer = 120 #R для точек откуда линии
    for k in range(m):
        A = ps2ds(S,(R_outer,fi))
        S = ps2ds((x,y),(R_outer,fi))

        sector_for_G(S[0], S[1],20, fi_for_sector, R+10)
        
        fi_for_sector -= 60
        fi -= df

one(200,200)
two(500,200)
B(200,500)
G(500,500)

root.mainloop()
