
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

longueur_noms = [len(nom) for nom in noms if len(nom)<10]
noms_avec_e = [nom for nom in noms if "e" in nom]
long_noms = [len(nom) if len(nom) < 10 else 0 for nom in noms]
a = [i for i in range(5)]
pair = [i for i in range(5) if (i//2)*2 == i]
b = [(i ,"Pair:", True if (i//2)*2 == i else False) for i in range(11)]

print(longueur_noms)
print(noms_avec_e)
print(long_noms)
print(a)
print(pair)
print(b)
