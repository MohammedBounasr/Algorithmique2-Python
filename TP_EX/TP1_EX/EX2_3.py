T=[0]*5
note=[0]*5
cof=[0]*5
scof=0
for i in range (5) :
    note[i] = float(input(f"enter la note de la matiere {i+1} "))
    cof[i] = int(input(f"enter le cofficient de matiere {i+1} "))
    T[i] = note[i]*cof[i]
    scof=cof[0]+cof[1]+cof[2]+cof[3]+cof[4]
moy=(T[0]+T[1]+T[2]+T[3]+T[4])/scof
print(f"la  moyen des matiers {moy}")