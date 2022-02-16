def demander_nom():
    nom = ""
    while nom == "":
        nom = input("Quel est votre nom ? : ")
    return nom


def demander_age(nom):
    age = 0
    while age == 0:
        try:
            age = int(input(nom + ", quel est votre age ? "))
        except ValueError:
            return ("ERREUR : Entrez un nombre pour l'age")
        else:
            return age

def demander_taille(nom):
    taille = 0
    while taille == 0:
        try:
            taille = float(input(nom + ", quel est votre taille ? "))
        except ValueError:
            return ("ERREUR : Entrez un float pour la taille")
        else:
            return taille

def print_info(nom, age, taille = 0):
    print(f"Vous vous appelez {nom}")
    print(f"Vous avez {str(age)} ans")
    print("L'année prochaine, vous aurez %s ans" % (age + 1))
    if not taille == 0:
        print(f"Votre taille est {str(taille)}.")


def majeur_info(age):
    if age >= 18:
        return True
    else:
        return False

"""
nom1 = demander_nom()
nom2 = demander_nom()

age1 = demander_age(nom1)
age2 = demander_age(nom2)

print()
print_info(nom1, age1)
print_info(nom2, age2)

print()
print("Etes-ce que " + nom1 + " est majeur ? : " + str(majeur_info(age1)))
print("Etes-ce que " + nom2 + " est majeur ? : " + str(majeur_info(age2)))
"""


for i in range(0, 2):
    nom = "personne" + str(i+1)
    try:
        age = demander_age(nom)
        taille = demander_taille(nom)
        print_info(nom, age, taille)
    except:
        print("ERREUR : review your code !")

print("""
Petit
        Test
                Sympa
""")

print("toto ", 20, "taille : ", 1.20, " m")
