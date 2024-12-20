
import math


a = float(input("Entrez le coefficient a (a ≠ 0) : "))
b = float(input("Entrez le coefficient b : "))
c = float(input("Entrez le coefficient c : "))

# Calcul du discriminant delta
delta = b**2 - 4*a*c


if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"Les solutions réelles de l'équation sont : x1 = {x1} et x2 = {x2}")
elif delta == 0:
    x = -b / (2 * a)
    print(f"La solution réelle double de l'équation est : x = {x}")
else:
    # Si le discriminant est négatif, les racines sont complexes
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-delta) / (2 * a)
    print(f"Les solutions complexes de l'équation sont :")
    print(f"x1 = {real_part} + {imaginary_part}i et x2 = {real_part} - {imaginary_part}i")
