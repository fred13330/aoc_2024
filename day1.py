# Lecture des données initiales
with open("data.txt") as fichier_initial:
    donnees_brutes = fichier_initial.readlines()

# Création d'une lise depuis donnees_brutes
# avec suppression des caractères parasites
donnees_initiales = [item.split() for item in donnees_brutes]

# Création des listes gauche et droites avec classement ascendant
liste_gauche = sorted([int(item[0]) for item in donnees_initiales])
liste_droite = sorted([int(item[1]) for item in donnees_initiales])

# Création de la liste des écarts
# Pour chaque index, on calcul la valeur absolue de la valeur gauche - valeur droite
liste_ecart = [abs(liste_gauche[index] - liste_droite[index]) for index in range(len(liste_gauche))]

# Création de la liste des similitudes
# Pour chaque item de la liste de gauche, on le mutiplie par le nombre d'item à droite
liste_similitudes = [liste_droite.count(item) * item for item in liste_gauche]

print("Partie 1 :", sum(liste_ecart))
print("Partie 2 :", sum(liste_similitudes))
