"""Personne.AutreFonction() # Méthode de Classe
personne1.SePresenter() # Méthode d'instance"""


class Personne():
    def __init__(self, nom : str = "", age: int = 0): #Constructeur qui stocke toutes les donées dans le self
        self.nom = nom
        self.age = age
        if nom == "":
            self.DemanderNom()
        print(f"La personne {self.nom} a été crée.")

    def SePresenter(self):
        info_personne = f"Bonjour, je m'appelle {self.nom}."
        
        if self.age > 0:
            info_personne += f"J'ai {str(self.age)} ans."

        print(info_personne)

        if self.age > 0:
            if self.EstMajeur() == True:
                print("Je suis majeur.")
            else:
                print("Je suis mineur.")

    def EstMajeur(self) : 
        return self.age >= 18

    def DemanderNom(self):
        self.nom = input("Quel est votre nom ?")



personne1 = Personne("Jean", 30)
personne2 = Personne("Paul", 0)
personne3 = Personne( age = 21)

personne1.SePresenter()
personne2.SePresenter()
personne3.SePresenter()



