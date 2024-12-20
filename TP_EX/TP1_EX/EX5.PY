    #EX5_1

x=int(input("enter un nombre entier"))
if x%2==0 :
    print(f"{x} est pair")
else :
    print(f"{x} est impair ")

    # EX5_2

    x=float(input("enter un nombre reel "))
y=float(input("ener un nombre reel "))
op=input("enter le symbOle de l'operation (+,-,*/) ")
if op=="+" :
    r=x+y
elif op=="-" :
    r=x-y
elif op=="*":
    r=x*y
elif op=="/" :
    r=int()
    try :
          r=x/y
    except :
        print("IMPOSIBLE")
        exit()
print(f"le resultat de l'operation est : {r}")