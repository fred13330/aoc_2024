def charger_donnees():

    # Chargement des données depuis le fichier data.txt
    with open("data.txt") as fichier_initial:
        donnees_brutes = fichier_initial.readlines()

    # Retour des données lues
    return donnees_brutes


def calculer_ecarts_listes(donnees_initiales):

    # Récupération des listes gauche et droite avec passage en numérique
    liste_gauche = [int(item[0]) for item in donnees_initiales]
    liste_droite = [int(item[1]) for item in donnees_initiales]

    # Initialisation du toal des écarts entre les listes
    total_ecart_entre_liste = 0

    # On boucle sur la liste tant qu'elle contient des éléments
    while len(liste_droite) > 0:

        # Récupération des minimas sur les deux listes
        minimun_gauche = min(liste_gauche)
        minimun_droite = min(liste_droite)

        # Ajout de la valeur absolue de la différence des minimas à la liste des écarts
        total_ecart_entre_liste += abs(minimun_gauche - minimun_droite)

        # Suppression des minimas déjà utilisés
        liste_gauche.remove(minimun_gauche)
        liste_droite.remove(minimun_droite)

    # Retour du total des écarts
    return total_ecart_entre_liste


def calculer_similitude(donnees_initiales):

    # Récupération des listes gauche et droite avec passage des valeurs en numérique
    liste_gauche = [int(item[0]) for item in donnees_initiales]
    liste_droite = [int(item[1]) for item in donnees_initiales]

    # Initialisation du total des similitudes
    total_similitudes = 0

    # On boucle sur la liste de gauche avec récupération du nombre
    # de similtudes dans la liste de droite
    for item in liste_gauche:
        nombre_equivalences = liste_droite.count(item)
        total_similitudes += item * nombre_equivalences

    # Retour du total des similitudes
    return total_similitudes


# Transformation des données lues en liste
# avec suppression des caractères parasites avant et après les éléments
donnees_initiales = [item.split() for item in charger_donnees()]

# Affichage des résultats
print("Partie 1 :", calculer_ecarts_listes(donnees_initiales))
print("Partie 2 :", calculer_similitude(donnees_initiales))
