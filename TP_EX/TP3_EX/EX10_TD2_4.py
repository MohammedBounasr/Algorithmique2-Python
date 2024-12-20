def power2(x):
    if x==1:
        p=1
    else:
        p=power2(x-1)+2*x-1
    return p
x=int(input("enter un nombre entier "))
print(f"la puissece de {x} est : { power2(x)}")
