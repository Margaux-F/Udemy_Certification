
personnes = ("Mélanie", "Martin", "Pierre", "Alice", "Jean")

# [start:stop:step]
for i in personnes[::2]:
    print(i)

nom = "Jean"
print(nom[::-1])



# ---------------------------------------
noms = []

while True:
    nom = input("Nom de la personne")
    if nom == "":
        break
    noms.append(nom)

print()
print("Noms des personnes")
noms.sort()
for nom in noms:
    print("   " + nom)



noms_et_distances = [("Patrick", 1.5), ("Paul", 0.3), ("Jean_Jacques", 32)]
distance_min = noms_et_distances[0][1] # [case 1 ou 2 dans ("Paul", 0.3)][numéro case de la liste]

nom_et_distance_min = noms_et_distances[0]
for nom_et_distance in noms_et_distances:
    if nom_et_distance[1] < nom_et_distance_min[1]:
        nom_et_distance_min = nom_et_distance

print("distance minimale : ", nom_et_distance_min[1], "nom du chauffeur : ", nom_et_distance_min[0])
