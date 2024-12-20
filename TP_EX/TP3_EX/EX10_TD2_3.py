def fact(x):
    if x==1 or x==0 :
        s= 1 
    else :
            s=x*fact(x-1)
    return s   
x=int(input("enter un nombre entier "))
print(f"la factoreile est : { fact(x)}")