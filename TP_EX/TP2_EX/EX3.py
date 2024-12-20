# Fonction pour lire les éléments d'un tableau
def lire_tab(t, n):
    for i in range(n):
        t[i] = int(input(f"Entrez la note numéro {i+1}: "))

# Fonction pour afficher les éléments d'un tableau
def afficher_tab(t, n):
    for i in range(n):
        print(f"Note de l'élève {i+1}: {t[i]}")

# Fonction pour calculer la somme des éléments du tableau
def sum_tab(t, n):
    s = 0
    for i in range(n):
        s += t[i]
    return s

# Fonction pour calculer la moyenne des éléments du tableau
def mean_tab(t, n):
    return sum_tab(t, n) / n

# Fonction pour trouver la valeur minimale dans le tableau
def min_tab(t, n):
    min_val = t[0]
    for i in range(1, n):
        if t[i] < min_val:
            min_val = t[i]
    return min_val

# Fonction pour compter les occurrences d'un élément dans le tableau
def nb_occurrence(t, n, elt):
    nb = 0
    for i in range(n):
        if t[i] == elt:
            nb += 1
    return nb

# Fonction pour vérifier si le tableau est trié
def is_sorted(t, n):
    is_sorted_asc = True
    is_sorted_desc = True
    for i in range(n - 1):
        if t[i] > t[i + 1]:
            is_sorted_asc = False
        if t[i] < t[i + 1]:
            is_sorted_desc = False

    if is_sorted_asc:
        print("Le tableau est trié dans l'ordre croissant.")
    elif is_sorted_desc:
        print("Le tableau est trié dans l'ordre décroissant.")
    else:
        print("Le tableau n'est pas trié.")

# Fonction de tri à bulles (naive sort)
def naive_sort(t, n):
    for i in range(n - 1):
        for j in range(i + 1, n):
            if t[i] > t[j]:
                # Échange des éléments
                temp = t[i]
                t[i] = t[j]
                t[j] = temp

# Exemple d'utilisation
n = int(input("Entrez le nombre d'élèves : "))
tab = [0] * n  # Créer un tableau de taille n

lire_tab(tab, n)
afficher_tab(tab, n)

# Vérification si le tableau est trié
is_sorted(tab, n)

# Tri du tableau
naive_sort(tab, n)
print("Après tri :")
afficher_tab(tab, n)
