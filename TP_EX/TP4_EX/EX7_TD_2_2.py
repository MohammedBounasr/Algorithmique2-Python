def nbrcons(phrase):
    if 
    cons="zrtpqsdfghjklmwxcvbn"
    s=0
    for char in  phrase:
        if char in cons:
            s+=1
    return s

x=input("enter une phrase ")
print(nbrcons(x))