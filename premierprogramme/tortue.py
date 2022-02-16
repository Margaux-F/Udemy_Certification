import turtle

t = turtle.Turtle()

def marche(nb_marches, taille):
    for i in range(nb_marches):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
        taille -= 10
    t.forward(taille)

try :
    nb_marches = int(input("Combien de marches voulez-vous ? : "))
except ValueError():
    print("ERREUR : Entrez un nombre !")

try :
    taille = int(input("De quelle taille ? : "))
except ValueError():
    print("ERREUR : Entrez un nombre !")
else: 
    marche(nb_marches, taille)

turtle.done()