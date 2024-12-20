def spnm (n):
    i=1
    j=1
    s=0
    while i <=n :
        j+=1
        if j%2==0 and j%3!=0 :
            s+=j
            i+=1
    return s
x=int(input("enter un nombre entier"))
print(f"la somme des {x} premiers nombers pairs non multiples de 3 est : {spnm(10)}")