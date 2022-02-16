#FONCTIONS AVANCEES 
#
#CALLBACKS


def mult_callback(a,b):
    return a*b

def add_callback(a,b):
    return a+b

def power_callback(a,b):
    return pow(a,b)

def afficher_table(n, operateur_str, operation_cbk):
    for i in range(1,10):
        print(i, operateur_str, n, "=", operation_cbk(i,n))

table = int(input("Quelle table voulez-vous ? : "))
print()
afficher_table(table, "x", mult_callback)
print()
afficher_table(table, "+", add_callback)
print()
afficher_table(table, "^", power_callback)