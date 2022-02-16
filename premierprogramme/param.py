# FONCTIONS AVANCEES
#
# Nombre variable de paramètres


def somme (titre, *args): #  *args récupère toutes les valeurs entrées
    resultat = 0
    print("TITRE = ", titre)
    for n in args:
        resultats += n
    return resultat

print(somme("somme des notes", 15, 4, 24))


def somme2(titre, **nombres):
    print("TITRE = ", titre)
    resultat = 0
    for n in nombres.values():
        resultat += n
    return resultat

print(somme("somme des notes", math = 13, geo=4))