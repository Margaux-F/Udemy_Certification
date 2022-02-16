personne = {"Nom" : "Margaux", "Age" : 20, "Taille" : 1.63}
print(personne)

print(personne['Nom'])

personne['Nom'] = 'Claire'
personne['Poste'] = 'Développeur'

personne['Achats'] = ('oeufs','banade', 'lait')

for i in personne:
    print(f"clef : {i} - valeur : {personne[i]}")
