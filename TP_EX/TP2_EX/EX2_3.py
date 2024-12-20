def max (x,y,z):
    maxn =x
    if maxn<y and y > z:
        maxn=y
        return maxn
    elif maxn < z and z>y :
        maxn=z
        return maxn
    else :
        return maxn
a=int(input("enter un monbre reel "))
b=int(input("enter un monbre reel "))
c=int(input("enter un monbre reel "))
print(f"le max de 3 entier est {max(a,b,c)}")