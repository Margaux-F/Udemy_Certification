

# ----------------- SORT -----------------------------

def tri_longueur_caracteres(noms):
    return len(noms)

noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe"]

noms_tries = sorted(noms)
noms_reverse = sorted(noms, reverse=True)
noms_sort = sorted(noms, key = lambda nom : len(nom))
# noms_sort = sorted(noms, key = tri_longueur_caracteres, reverse=True)

print(noms)
print(noms_tries)
print(noms_reverse)
print(noms_sort)

