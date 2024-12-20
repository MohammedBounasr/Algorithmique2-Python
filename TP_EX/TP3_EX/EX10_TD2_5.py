def pgcd(a,b):
    if b==0:
        p=a
    elif a%b!=0 :
        b=a%b
        
        





x=int(input("enter un nombre entier "))
y=int(input("enter un nombre entier "))
print(f"le pgcd de {x} et {y} est : { pgcd(x,y)}")