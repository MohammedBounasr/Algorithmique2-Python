from math import *
def fct (x):
   f= x**5-abs(1-sqrt(x**2))+1/(1+x**2)
   return f
a=float(input("enter un nombre "))
print(fct(a))