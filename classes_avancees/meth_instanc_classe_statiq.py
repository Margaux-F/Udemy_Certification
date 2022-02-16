class Personne:
    TYPE = "Humain"
    def __init__(self, nom):
        self.nom = nom
    
    # Méthode d'instance
    def SePresenter(self):
        print(f"Je m'appelle {self.FormaterChaine(self.nom)} - {self.TYPE}.")

    # Premier caractère en maj puis minuscules
    # Méhode statique
    @staticmethod
    def FormaterChaine(a):
        return a[0].upper() + a[1:].lower()

    @classmethod
    def methode_de_classe(cls):
        print("Méthode de classe" + cls.TYPE)

personne1 = Personne("jean")
personne1.SePresenter()

print(Personne.FormaterChaine("tOtO"))