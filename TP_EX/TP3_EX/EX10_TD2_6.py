def pgcd(a,b):
    if b==0:
        p=a
    else:
       p= pgcd(b,a%b)
    return p
x=int(input("enter un nombre entier "))
y=int(input("enter un nombre entier "))