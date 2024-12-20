def suite (n):
    if n==0:
        u=1
    else:
        u=2*suite(n-1)
    return u
def som(n):
    i=0
    S=0
    while i <=n :
        S+=suite(i) # s=s+suite
        i+=1
    return S
x=int(input("enter un nomnre n"))
print(f"la somme de term {x} est : {som(x)}")