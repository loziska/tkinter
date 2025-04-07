
from math import *
def create_circle(obj, S, R,**params):
    (xs,ys) = S
    return obj.create_oval(xs-R,ys-R,xs+R,ys+R,params)

# функция перехода к декартовым координатам
def ps2ds(S,L):
    (xs,ys)=S
    if type(L) == tuple:
        (R,fi)=L
        return (xs + R*cos(pi*fi/180), ys - R*sin(pi*fi/180))
    if type(L) == list:
        return [(xs + R*cos(pi*fi/180), ys - R*sin(pi*fi/180)) for (R,fi) in L]
    
# функция перехода к полярным координатам
def ds2ps(S,L):
    (xs,ys)=S
    grd =180/pi
    if type(L) == tuple:
        (x,y)=L
        return (sqrt((x-xs)**2+(y-ys)**2), -atan2(y-ys,x-xs)*grd)
    if type(L) == list:
        return [(sqrt((x-xs)**2+(y-ys)**2), -atan2(y-ys,x-xs)*grd) for (x,y) in L]
    
# сложение векторов в экранной системе координат
def add(S,*L):
    (xs, ys)=S
    for (x,y) in L:
        xs=xs+x
        ys=ys+y
    return (xs, ys)

# умножение векторов на число в экранной системе
def mlt(L,k):
    if type(L)==list:
        return [mlt(P,k) for P in L]
    else:
        (x,y)=L
        return (x*k, y*k)
    
# поворот списка точек на заданный угол
def turn(S, L, df):
    P = ds2ps(S,L)
    if type(P)==tuple:
        (R,fi)=P
        return ps2ds(S,(R,fi+df))
    if type(P)==list:
        W=[(R,fi+df) for R,fi in P]
        return ps2ds(S,W)
    
# сдвиг списка точек на заданный вектор
def move(V, L):
    if type(L)==list:
        return [add(V,P) for P in L]
    else:
        return add(V,L)
    
# зеркальное отображение списка точек
def symmetry(P,Q,L):
    (rq,fq)=ds2ps(P,Q)
    if type(L)==tuple:
        (rw,fw)=ds2ps(P,L)
        return (ps2ds(P,(rw,2*fq-fw)))
    if type(L)==list:
        res=[]
        for W in L:
            (rw,fw)=ds2ps(P,W)
            res.append(ps2ds(P,(rw,2*fq-fw)))
        return res

