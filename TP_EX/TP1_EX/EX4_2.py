
a = int(input("Entrez la valeur de a: "))
b = int(input("Entrez la valeur de b: "))
c = int(input("Entrez la valeur de c: "))


print(f"Avant permutation : a = {a}, b = {b}, c = {c}")


temp = a
a = c
c = b
b = temp


print(f"Après permutation : a = {a}, b = {b}, c = {c}")
