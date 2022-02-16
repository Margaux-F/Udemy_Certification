

def poser_questions(question, r1, r2, r3, r4, choix_bonne_reponse):
    global score
    print("score :", score)
    print("QUESTION")
    print("   " + question)
    print("   (a)", r1)
    print("   (b)", r2)
    print("   (c)", r3)
    print("   (d)", r4)
    print()
    reponse = input("Votre réponse : ")
    if reponse == choix_bonne_reponse:
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse")

    print()

score = 0
poser_questions("Quelle est la capitale de la France ?", "Paris", "Marseille ", "Lyon", "Nice", "a")
poser_questions("Quelle est la capitale de l'Italie ?", "Venise", "Pise", "Rome", "Florence", "c")

print("Score final :", score)