from ast import Lambda
import math
def fun(y=lambda x:x-math.sin(x), a=-1, b=1, toll=0.0001):
    while abs(a-b)>=toll:
        c=(a+b)/2
        if y(a)*y(c)<=0:
            b=c
        if y(c)*y(b)<=0:
            a=c
    print(c)
fun() 