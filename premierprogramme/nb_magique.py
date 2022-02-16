# Margaux Faurie
# 14 février 2022

from random import randint

def demand_nb(nb_min, nb_max):
    try : 
        while True:
            nb_choisi = int(input(f"Saisissez un nombre entre {nb_min} et {nb_max}: "))
            if nb_min <= nb_choisi <= nb_max :
                return nb_choisi
            else:
                print("Le choix n'est pas possible ! il n'est pas dans l'intervalle, reréfléchissez...")
        
    except ValueError():
        print("ERREUR : Entrez un nombre !")

def bornes():
    demand = False
    while demand == False:
        try : 
            min = int(input("Borne minimale de l'intervalle ? :"))
            max = int(input("Borne maximale de l'intervalle ? :"))
            if min < max:
                demand = True
            else : 
                min = "error"
        except ValueError():
            print("ERREUR : Entrez un nombre correct !")
    return min, max




# Détermine les bornes de l'intervalle
min, max = bornes() 
print(f"Les bornes de l'intervalle contenant nb_magique sont {min} et {max}.")

# Choix du nb_magique aléatoirement
nb_magique = randint(min, max)
print("nb à trouver", nb_magique)

# Initialisation game
game = False 

# Déterminer nombre de vies
essais = True
while essais == True:
    try :
        nb_essai = int(input("Combien d'essais voulez-vous ? :"))
        if nb_essai <=0 :
            print("nb_essai négatif, ce n'est pas possible ! \n")
        else:
            essais = False
    except ValueError():
        print("ERREUR : Rentrez un nombre d'essais valide !\n")

# Jeu 
essai = 0
while game == False and essai < nb_essai:
    demand = demand_nb(min, max)
    if demand > nb_magique:
        print("Plus petit ! ")
    elif demand < nb_magique:
        print("nb_magique est plus grand ! ")
    else:
        game = True
        print(f"Le nombre trouvé est {str(nb_magique)}, vous avez gagné, bravo !")
    essai += 1
    print(f"Nombre d'essais : {essai} \n")
    if essai == nb_essai -1 :
        print("Dernier essai !")
    elif essai == nb_essai:
        print("Nombre d'essais possible dépassés. Désolée !")
