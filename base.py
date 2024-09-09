# Revision rapide des bases en Python

# 1. Variables et Types
x = 10 # int
y = 10.0 # float
nom = "Sleyter"
validation = True # bool
liste = [1, 2, 3, 4, 5] # list
coordonnees = (10, 20) # tuple
identite = {"nom": "Sleyter", "age": 22} # dict
nombre_unique = {1, 2, 3, 4, 5} # set

# 2. Structures de contrôle

#egal ==
#different !=
#inferieur <
#superieur >
#inferieur ou egal <=
#superieur ou egal >=
#et and
#ou or
#non not

nb1=int(input("Entrez un nombre entre 10 et 20 : "))
nb2=int(input("Entrez un deuxieme nombre : "))
nb3=int(input("Entrez un troisieme nombre : "))

if ((nb1 == nb2) or (nb2 == nb3) or (nb1 == nb3) and not nb1 == nb2 == nb3):
    print("Il y a au moins deux nombres identiques")
else:
    print("Il n'y a pas de nombres identiques")

if x == 10:
    print("x est égal à 10")
elif x > 10:
    print("x est supérieur à 10")
else:
    print("x est inférieur à 10")
    
add = input("Entrez une adresse IP\n")
add=add.split(".")
add.pop()
add=".".join(add)
for fin in range(1, 255):
    print(add+"."+str(fin), end="\t")

import time    
nb_while =int(input("Entrez un nombre\n"))
while(nb_while > 0):
    print(nb_while)
    nb_while=nb_while-1
    time.sleep(0.5)

# 3. Fonctions
def presentation(nom):
    return f"Bonjour, {nom} !"

print   (presentation("Sleyter"))

# 4. Classes et Objets
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        
    def presentation(self):
        return f"Bonjour, je m'appelle {self.nom} et j'ai {self.age} ans."  
    
sleyter = Personne("Sleyter", 22)
print(sleyter.presentation())