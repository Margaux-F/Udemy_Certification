import copy

class Personne:
    def __init__(self, nom, age,amis):
        self.nom = nom
        self.age = age
        self.amis = amis

    def AfficherInfos(self):
        print(f"Je m'appelle {self.nom} et j'ai {self.age} ans.")
        print(f"Amis : {str(self.amis)}.")

    def __eq__(self, other):
        return self.nom == other.nom and self.age == other.age

    #def __str__(self):
    #    return "STR"

    def __repr__(self):
        return __class__.__name__ + " " + str(self.__dict__)

personne1 = Personne("Jean", 20, ["Pierre", "Paul", "Jacques"])
personne1.AfficherInfos()

personne2 = copy.copy(personne1) #Attention : une shallow copy change donne juste le lien, et ne prend pas uniquement les données -> si on change le 1 on change aussi le 2
personne3 = copy.deepcopy(personne1) #Fais une deep copy -> prend toutes les infos et non le lien
#personne1.nom = "Toto"
personne1.amis[0] = 'Chantale'
personne2.AfficherInfos()
personne3.AfficherInfos()

print(personne1 == personne2)
print(personne1 is personne2)

print(personne1.__dict__ == personne2.__dict__)

print(personne1)
