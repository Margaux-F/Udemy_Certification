# LES COLLECTIONS : LISTES / TUPLES
# Append / Extend / += / Insert

# ----------------- LISTES -----------------------------

noms = ["Jean", "Sophie", "Martin"]

noms_supp = ["Christophe", "Zoe"]

# noms.append(noms_supp)
# for e in noms_supp:
#   noms.append(e)

#noms.extend(noms_supp)
# noms += noms_supp # Equivalent à extend

# noms.insert(1,"Toto")

noms = ["Toto"] + noms + noms_supp


# ----------------- SLICES -----------------------------
print(noms)
print(noms[::2])


slice_noms = noms[:] #Fais une copie de la liste
# != slices_noms = noms # La liste est identique

noms[0] = "JP"

print(slice_noms)
print(noms)

