
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

# Prend moins de mémoire, avec liste, len et sum

longueur_noms = [len(nom) for nom in noms]
print("Nombre de caractères : ", sum(longueur_noms))

#Avec join et len()

print("Nombre de caractères :", len("".join(noms)))

