def afficher_infos_personnes(nom="", age = 0):
    if nom == "":
        print(f"Vous n'avez pas donné de nom, l'age est {age}")
    else:
        print(f"La personne est {nom}, agée de {age} ans")
        print("Le nom comporte", len(nom), "caractères")

afficher_infos_personnes(age = 20)

afficher_infos_personnes("Jean", 20)