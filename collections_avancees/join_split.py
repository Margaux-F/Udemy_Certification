
# ----------------- JOIN -----------------------------

noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe"]

noms_joins = " - ".join(noms)

print(noms_joins)



# ----------------- SPLIT -----------------------------

a = "Paul-Marc-Sophie"

a_split = a.split("-")

print(a_split)



# ----------------- INDEX -----------------------------

#Donne l'index de la première valeur de "Sophie"
print(noms.index("Sophie"))

# noms.index("Sophie", 3) #Cherche "Sophie à partir de l'index 3"



# ----------------- OCCURENCES ------------------------

noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

element_recherche = "Martin"
nb_occurences = noms.count(element_recherche)
print("nb_occurences", nb_occurences)
if nb_occurences > 0:
    index_occurence = 0
    for i in range(nb_occurences):
        index_occurence = noms.index(element_recherche, index_occurence)
        print(element_recherche, "trouvé à", index_occurence)
        index_occurence += 1
else:
    print("L'élément n'est pas dans la collection")

# ----------------- FIND ------------------------

a = "Martin-Jean-Toto"
print(a.find("Jean"))

