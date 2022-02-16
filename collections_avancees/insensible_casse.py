
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

def element_dans_liste(noms, element_recherche):
    noms = [nom.lower() for nom in noms]
    return element_recherche in noms


print(element_dans_liste(noms, "martin"))