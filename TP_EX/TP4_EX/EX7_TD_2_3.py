def distance_hamming(char1,char2):
    if len(char1)!=len(char2):
         return("invalide valeur")
    n=0
    for i in range(len(char1)):
        if char1[i]!=char2[i] :
            n+=1
    return n
x=input("enter une mot ")
y=input("enter une mot ")
print(distance_hamming(x,y))