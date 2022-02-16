
pizzas_noms = ("4 fromages", "calzone", "Hawaï")
pizzas_prix = (10.5, 11, 8)

noms_et_prix = list(zip(pizzas_noms, pizzas_prix))

for (nom, prix) in zip(pizzas_noms, pizzas_prix):
    print(f"{nom} - {prix}")

unzipped = list(zip(*noms_et_prix)) # * sépare tous les éléments comme précédemment, le zip rassemble les 1er éléments
pn, pp = list(zip(*noms_et_prix))

print(noms_et_prix)
print(unzipped)

