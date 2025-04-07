from math import sin, cos, pi, sqrt, atan2

def ps2ds(S,L):
    """
    S - центр системы координат
    L - точка (кортеж) или список точек (кортежей)
    в полярной системе координат с центром в точке S
    результат - точка (кортеж) или список точек (кортежей)
    в экранной системе координат
    """
    (xs,ys)=S
    if type(L) == tuple:
        (R,fi)=L
        return (xs + R*cos(pi*fi/180), ys - R*sin(pi*fi/180))
    if type(L) == list:
        return [(xs + R*cos(pi*fi/180), ys - R*sin(pi*fi/180)) for (R,fi) in L]

def ds2ps(S,L):
    """
    S - центр системы координат
    L - точка (кортеж)или список точек (кортежей)
    в экранной системе координат
    результат - точка (кортеж) или список точек (кортежей)
    в полярной системе координат с центром в точке S
    """
    (xs,ys)=S
    grd =180/pi
    if type(L) == tuple:
        (x,y)=L
        return (sqrt((x-xs)**2+(y-ys)**2),-atan2(y-ys,x-xs)*grd)
    if type(L) == list:
        return [(sqrt((x-xs)**2+(y-ys)**2), -atan2(y-ys,x-xs)*grd) for (x,y) in L]

def turn(S, L, df):
    """
    S - центр поворота
    L - точка (кортеж) или список точек (кортежей)
    df - угол поворота. При df>0 поворот против часовой
    стрелки, при df<0 - по часовой стрелке
    результат - точка (кортеж) или список точек (кортежей)
    после поворота
    """
    P = ds2ps(S,L)
    if type(P)==tuple:
        (R,fi)=P
        return ps2ds(S,(R,fi+df))

    if type(P)==list:
        W=[(R,fi+df) for R,fi in P]
        return ps2ds(S,W)


def norm_sector(x,y, center_for_dyga, n, u0, R):
    '''dx, dy - на сколько смещать точку относительно центра
    из которой рисуется обводочка сектора'''
    S = (x,y)
    
    # задаём параметры разбиения
    (xa,ya) = S # точка выхода лучей
    (xs,ys) = center_for_dyga
    u0=u0-90 #u0 с какого угла начинается дуга у сектора
    du=180 #du сколько она длится, у нас это 360/ на 6 лепестков
    # рисуем узор
    canvas.create_arc(xs-R,ys-R,xs+R,ys+R,start=u0,extent=du,style=ARC)

    m = 6; df = 180/m; fi=0
    for k in range(n+1):
        fi = u0 + (k/n)*du
        (x,y) = ps2ds((xs,ys),(R,fi))
        canvas.create_line(xa,ya,x,y)

def sector_for_G(x,y, n, u0, R):
    '''dx, dy - на сколько смещать точку относительно центра
    из которой рисуется обводочка сектора'''
    S = (x,y)
    
    # задаём параметры разбиения
    (xa,ya) = S # точка выхода лучей
    (xs,ys) = S
    u0=u0 #u0 с какого угла начинается дуга у сектора
    du=70 #du сколько она длится, у нас это 360/ на 6 лепестков
    # рисуем узор
    canvas.create_arc(xs-R,ys-R,xs+R,ys+R,start=u0,extent=du,style=ARC)

    m = 6; df = 180/m; fi=0
    for k in range(n+1):
        fi = u0 + (k/n)*du
        (x,y) = ps2ds((xs,ys),(R,fi))
        canvas.create_line(xa,ya,x,y)
