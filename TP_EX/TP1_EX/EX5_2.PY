# calculator
x=float(input("enter un nombre reel "))
y=float(input("ener un nombre reel "))
op=input("enter le symbole de l'operation (+,-,*/) ")
if op=="+" :
    r=x+y
elif op=="-" :
    r=x-y
elif op=="*":
    r=x*y
elif op=="/" :
    try :
          r=x/y
    except :
        print("IMPOSIBLE")
        exit()
print(f"le resultat de l'operation est : {r}")