from math import *
def fctm (x) :
    if x >= 0 :
        f = sqrt(x)+2
        return f
    elif x < 0 :
       f = (-x)**5
       return f
a=float(input("enter un nombre reel"))
print(f"l'emage de {a} est : {fctm(a)} ")
