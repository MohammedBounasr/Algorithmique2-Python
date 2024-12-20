def suite (n):
    if n==0: # la base 
        u=1
    else:
        u=2*suite(n-1)#   la base  و  هايك هيn =0 كيبقا يرجع بالوراء حتي كتولي 
    return u
x=int(input("enter un nombre entier "))
print(f"la valeur de la term {x} est : {suite(x)}")