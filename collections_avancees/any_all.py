
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]


a = [False, False, True, False]
print(any(a))
print(all(a))


found = False
for nom in noms:
    if "z" in nom.lower():
        found = True
        break

if found:
    print("Trouvé")
else:
    print("Non trouvé")



nom_avec_un_z = any([True if "z" in nom.lower() else False for nom in noms])
if nom_avec_un_z:
    print("Trouvé")
else:
    print("Non trouvé")