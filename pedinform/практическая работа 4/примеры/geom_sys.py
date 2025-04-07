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
