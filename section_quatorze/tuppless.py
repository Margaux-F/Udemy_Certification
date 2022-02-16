


a = 5
b = "toto"

personnes = ("Mélanie", "Jean", "Martin", "Alice")

print(personnes[0])
print(len(personnes))

for i in range(len(personnes)):
    print(personnes[i])

#range est un tupple des éléments en range(0,10) !
# Attention : tupples non modifiable != listes


#--------------------------------------
def obtenir_infos():
    return "Mélanie", 37, 1.60

def afficher_infos(nom,age,taille):
    print(f"informations : nom {nom}, age:{age}, taille={taille}")

infos = obtenir_infos()
afficher_infos(*infos)

