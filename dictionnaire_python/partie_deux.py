personnes = [
    ("Mélanie", 25, 1.6),
    ("Paul", 28, 1.82),
    ("Jean", 45, 1.7),
    ("Martin", 17, 1.9)
]

def obtenir_infos(nom, liste):
    for i in liste:
        if i[0] == nom:
            return i
    return None

infos = obtenir_infos("Martin", personnes)
#print(infos)

personnes_dict = {
     "Mélanie" : (25, 1.6),
     "Paul" : (28, 1.82),
     "Jean": (45, 1.7),
     "Martin": (17, 1.9)
}

infos = personnes_dict.get["Martin"]
if not infos:
    print("La clef n'existe pas")
else:
    print(infos)