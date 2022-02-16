def afficher(collection, nb_pizza =-1):
    # Liste des pizzas
    print(f"---- LISTE DES PIZZAS ({len(collection)}) ----")
    if len(collection) == 0:
        print("        Aucune pizza")
        return
    else:
        if not nb_pizza == -1 and nb_pizza < len(collection):
            collection = collection[:nb_pizza]
        else:
            print("Nombre de pizza à afficher non valide, on affiche tout")
        for i in collection:
            print("        ", i)
        print()
        print("Première pizza :", collection[0])
        print("Dernière pizza :", collection[-1])
        return

def add_pizza(collection):
    new_pizza = input("Pizza à ajouter : ")
    new_pizza.lower()
    if exist_pizza(new_pizza, collection) == False:
        collection.append(new_pizza)
        print(f"La pizza {new_pizza} a été ajoutée !")
        print("Nouvelle liste de pizzas : ")
        print(collection)
    else:
        print("ERROR : La pizza existe déjà")
    return collection.sort()

def exist_pizza(pizza, collection):
    exist = False
    for i in collection:
        if pizza == i:
            exist = True
    return exist
#if new_pizza in collection: print("cette pizza existe déjà") suffit !

def tri_personnalise(a):
    return a

pizzas = ["4 fromages", "végétarienne", "hawaï", "calzone"]
pizzas.sort(key = tri_personnalise) #On aurait pu aussi mettre par exemple reverse = True
for i in pizzas:
    i.lower()
vide = ()
afficher(pizzas, 5)
add_pizza(pizzas)