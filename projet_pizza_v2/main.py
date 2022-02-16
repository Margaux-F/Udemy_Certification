
def tri_nom(e):
    return e.nom

def tri_prix(e):
    return e.prix

def tri_nb_ingredients(e):
    return len(e.ingredients)



class Pizza():
    def __init__(self, nom : str, prix : float, ingredients, vegetarien = False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarien = vegetarien

    def Afficher(self):
        veg_str = ""
        if self.vegetarien:
            veg_str = " - VEGETARIENNE"

        print(f"\nPIZZA {self.nom} : {self.prix} €" + veg_str)
        print(f"Ingrédients :", ", ".join(self.ingredients))
        print()

class PizzaPersonnalisee(Pizza):
    prix_base = 7
    prix_ingredient = 1.2
    dernier_numero = 0
    
    def __init__(self):
        PizzaPersonnalisee.dernier_numero += 1
        self.numero = PizzaPersonnalisee.dernier_numero
        super().__init__(f"Personnalisée {str(self.numero)}", 0,[])
        self.demander_ingredient_util()
        self.calculer_prix()

    def demander_ingredient_util(self):
        while True:
            print()
            print(f"Ingrédients pour la pizza personnalisée n° {self.numero} :")
            ingredient = input("Ajoutez un ingrédient (ou ENTRER pour terminer) ! : \n")

            if ingredient == "":
                return
            
            self.ingredients.append(ingredient)
            print(f"Vous avez {len(self.ingredients)} ingrédients : {', '.join(self.ingredients)}")

    def calculer_prix(self):
        self.prix = len(self.ingredients) * self.prix_ingredient + self.prix_base









pizzas = [
     Pizza("4 fromages", 8.5, ("brie", "emmental", "compté", "parmesan"), True),
     Pizza("Chèvre miel", 11, ("chèvre", "miel", "lardons", "crème")),
     Pizza("Hawaï", 10.5, ("ananas", "tomate", "oignons", "lardons")),
     Pizza("Végétarienne", 9, ("champignons", "tomate", "oeuf", "poivron"), True),
     PizzaPersonnalisee(),
     PizzaPersonnalisee()

]




# pizzas.sort(key = tri_prix, reverse = True)

for i in pizzas:
    i.Afficher()


"""for i in pizzas:
    if not "tomate" in i.ingredients:
        #i.Afficher()
        pass
    if i.prix > 10:
        i.Afficher()"""

