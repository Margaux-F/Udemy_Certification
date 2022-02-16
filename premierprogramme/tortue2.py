import turtle

t = turtle.Turtle()

def carre(taille, nb_carre):
    for i in range(nb_carre):
        for i in range(4):
            t.forward(taille)
            t.left(90)
        taille += 10

taille = int(input("Quelle taille voulez-vous ? : "))
nb_carre = int(input("Combien de carrés ? : "))
carre(taille, nb_carre)

turtle.done()