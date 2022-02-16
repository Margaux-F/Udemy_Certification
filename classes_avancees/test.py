import random
 
sujets = ("un chasseur", "une grand mère", "un chat")
verbes = ("mange", "écrase", "parle à")
complements = ("une vache", "un char", "une fleur")
 
def generer_phrases(donnees, nb_phrases = 0):
    phrases = []
 
    if nb_phrases == 0:
        nb_phrases = len(donnees[0]) * len(donnees[1]) * len(donnees[2])
    
    while len(phrases) < nb_phrases:
        sujet = donnees[0][random.randint(0, len(donnees[0])-1)]
        verbe = donnees[1][random.randint(0, len(donnees[1])-1)]
        complement = donnees[2][random.randint(0, len(donnees[2])-1)]
 
        phrase = sujet + " " + verbe + " " + complement
        if not phrase in phrases:
            phrases.append(phrase)
 
    return phrases
 
 
phrases_generees = generer_phrases((sujets, verbes, complements))
 
print(len(phrases_generees), "phrases générées")
for p in phrases_generees:
    print(p)