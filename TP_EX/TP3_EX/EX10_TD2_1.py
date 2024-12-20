def power(a,n):
    if  n==0 :#la base هادي هي 
        p=1
    elif n< 0 : #قاعدة الاس السالب
        p=1/power(a,-n) #  باش داك الناقص مع الناقص كيولي موجب
    else :
        p=power(a,n-1)*a
    return p
a=float(input("enter un nombre "))
n=int(input("ener la puissence "))
print(f"la puissence de {a} a la puissence {n} est : {power(a,n)}")
  
  
    # exemple power(3,3)=
#power(3,3)=power(3,2)*3=1*3*3*3
#power(3,2)=power(3,1)*3= 1*3*3
#power(3,1)=power(3,0)*3 = 1*3
#power(3,O)=1 la base (finich recursive)

    # exemple power(3,-2)=
#power(3,-2)= 1/3^(-(-2)) 
