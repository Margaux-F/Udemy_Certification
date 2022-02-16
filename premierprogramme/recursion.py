#FONCTIONS : NOTIONS AVANCEES
#
# FONCTIONS RECURSIVES

def a(n):
    print("n : ", n)
    a(n*n)
    if a(n)>20:
        return 