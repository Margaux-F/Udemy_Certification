
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe"]

ages = [21, 20, 30, 25, 22]

# print(min(noms))
print(noms)

"""if "Jean" in noms:
    print("Présent")
else:
    print("Absent")"""

noms[0], noms[4] = noms[4], noms[0]
print(noms)
