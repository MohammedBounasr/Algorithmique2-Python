def surface (a,b,h):
    s=(a+b)*(h/2)
    return s
x=float(input("entrer la base infereur "))
y=float(input("entrer la base seperieur "))
z=float(input("entrer la base hoteur "))
print(f"la surface est {surface(x,y,z)}")