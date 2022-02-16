class Eleve():
    def __init__(nom, cours_inscrit):
        self.nom = nom
        self.cours_inscrit = cours_inscrit
 
    def afficher_infos(self):
        print("Eleve : " + self.nom)
        for cours in self.cours_inscrit:
            print(cours.get_description())
 
class Cours:
    def __init__(titre, nb_heures):
        self.titre = titre
        self.nb_heures = nb_heures
 
    def get_description(self):
        return self.titre + " (" + int(self.nb_heures) + " heures)"
 
cours_martin = (Cours("Maths Spe 1", 5),
                Cours("Anglais LVL2", 8),
                Cours("Chimie TP", 4))
 
e = Eleve("Martin")
e.afficher_infos()