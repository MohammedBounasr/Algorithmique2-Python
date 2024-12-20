def nbrvoy(phrase):
    voy="AEYUIOaeyuio"
    s=0
    for char in  phrase:
        
        if char in voy:
            s+=1
    return s

x=input("enter une phrase")
print(nbrvoy(x))