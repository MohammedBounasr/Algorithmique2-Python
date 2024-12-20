def som (n):
    s=0
    for i in range(1,n+1):
        s+=i
    return s
x=int(input("enter un nombre entier "))
print(f"la somme des termes est {som(x)}")

