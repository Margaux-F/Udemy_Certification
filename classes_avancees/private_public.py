# Modificateur d'accès : Public, private, protected

# public acces dpuis l'intérieur et l'extérier
# private : acces depuis l'intérieur uniquement __nom
# protected : acces depuis interieur classe et classes dérivées


class Personne:
    def __init__(self, nom):
        #private
        self._nom = nom

    def se_presenter(self):
        print(f"Je m'appelle {self._nom}")

class Etudiant(Personne):
    def se_presenter(self):
        print(f"Je suis étudiant, je m'appelle {self._nom}.")

personne1 = Etudiant("Jean")
personne1.se_presenter()

print(personne1.__dict__)
