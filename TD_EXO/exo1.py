"""
Question A 
Écrire le code Python  d’une fonction qui à partir de deux entiers (a et b) passés en 
paramètres (strictement positifs et formés chacun de deux chiffres) retourne un entier de 4 
chiffres tel que le nombre b est intercalé entre les deux chiffres de a. Exemple : Paramètres 
de la fonction : 
a=56, b=21 Résultat : 5216
"""

def intercaler(a, b):
    return int(str(a)[0] + str(b) + str(a)[1])

print(intercaler(56, 21)) # 5216

"""
Question B 
Écrire le code Python d’une fonction (saisieInt) qui admet 2 valeurs entières en paramètre 
(min et max), la fonction demandera à l’utilisateur de saisir une valeur entière comprise 
entre min et max, tant que la valeur saisie est erronée la fonction redemande la saisie. 
Quand la valeur saisie est correcte elle est renvoyée par la fonction. 
"""

min = 10
max = 20

def saisieInt(min, max):
    while True:
        try:
            val = int(input(f"Entrez une valeur entre {min} et {max} : "))
            if min <= val <= max:
                return val
        except ValueError:
            pass
saisieInt(min, max)