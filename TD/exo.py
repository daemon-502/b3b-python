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

"""
Question C 
Écrire le programme principal qui demande à l’utilisateur de saisir deux entiers compris dans 
l’intervalle [10 , 99] et qui affiche le nombre retourné par la fonction de la question 
précédente avec en paramètres les valeurs saisies. 
"""

"""
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

"""
Question C 
Écrire le programme principal qui demande à l’utilisateur de saisir deux entiers compris dans 
l’intervalle [10 , 99] et qui affiche le nombre retourné par la fonction de la question 
précédente avec en paramètres les valeurs saisies. 
"""

# Programme principal
a = saisieInt(10, 99)
b = saisieInt(10, 99)
input("Appuyez sur une touche pour afficher le résultat")
print(intercaler(a, b))

""" Nombre aléatoire : 
import random 
nombreDeBase = random.randint(1,1000) 
 
Question B 
Écrire le code d’un programme python qui va essayer de deviner le nombre 
choisi mentalement par l’utilisateur (compris entre 1 et 99). À chaque tour le 
programme fera une proposition de nombre à l’utilisateur qui devra répondre : 
— 1 : pour "valeur proposée trop petite" 
— 2 : pour "valeur proposée trop grande" 
— 3 : pour "valeur trouvée
"""

import random

def deviner():
    min = 1
    max = 100
    nb = random.randint(min, max)
    print(f"Je propose le nombre {nb}")
    while True:
        rep = input("1 : trop petit, 2 : trop grand, 3 : trouvé ? ")
        if rep == "1":
            min = nb
        elif rep == "2":
            max = nb
        elif rep == "3":
            print("Gagné")
            break
        nb = random.randint(min, max)
        print(f"Je propose le nombre {nb}")

deviner()

"""
Exercice 4 : les dictionnaires 
 
Soit le dictionnaire suivant : 
                                                 Exercices                                                           EBEL Franck 
Fondamentaux de la Programmation 
 
points_lettres={"A":1,"B":3,"C":3,"D":2,"E":1,"F":4,"G":2,"H":
4,"I":1,"J":8,"K":10,"L":1,"M":2,"N":1,"O":1,"P":3,"Q":8,"R":1
,"S":1,"T":1,"U":1,"V":4,"W":10,"X":10,"Y":10,"Z":10} 
 
Question 1 : 
Écrire une définition (comptePoints() ) qui prend un mot en majuscule en paramètres 
et renvois le nombre de points de ce mot. 
 
"""

points_lettres={"A":1,"B":3,"C":3,"D":2,"E":1,"F":4,"G":2,"H":
4,"I":1,"J":8,"K":10,"L":1,"M":2,"N":1,"O":1,"P":3,"Q":8,"R":1
,"S":1,"T":1,"U":1,"V":4,"W":10,"X":10,"Y":10,"Z":10}

def comptePoints(mot):
    return sum([points_lettres[lettre] for lettre in mot])

print(comptePoints("SLEYTER"))

"""
Question 2 : 
Écrire un programme principal qui demande à l’utilisateur un mot puis met ce mot en 
majuscule et qui appelle comptePoints afin d’afficher le nombre de points
"""

mot_user = input("Entrez un mot en MAJUSCULE : ")
mot_user = mot_user.upper()
print(comptePoints(mot_user))

"""
Question 3 : 
Écrire une définition (nbr_Consonnes ) qui compte le nombre de voyelles et de 
consonnes du mot donné par l’utilisateur. 
"""

def nbr_Consonnes(mot):
    voyelles = "AEIOUY"
    consonnes = "BCDFGHJKLMNPQRSTVWXZ"
    nb_voyelles = sum([1 for lettre in mot if lettre in voyelles])
    nb_consonnes = sum([1 for lettre in mot if lettre in consonnes])
    return nb_voyelles, nb_consonnes

consonnes_user = input("Entrez un mot : ")
print(nbr_Consonnes(consonnes_user))

"""
Question 5 : 
Nous voulons maintenant compter le nombre de points des voyelles puis des 
consonnes du mot donné par l’utilisateur. 
Ajoutez/modifiez votre programme afin de répondre à cette question
"""

def comptePointsVoyellesConsonnes(mot):
    points_voyelles = sum([points_lettres[lettre] for lettre in mot if lettre in "AEIOUY"])
    points_consonnes = sum([points_lettres[lettre] for lettre in mot if lettre in "BCDFGHJKLMNPQRSTVWXZ"])
    return points_voyelles, points_consonnes

mot_user1 = input("Entrez un mot : ")
print(comptePointsVoyellesConsonnes(mot_user1))

points_voyelles, points_consonnes = comptePointsVoyellesConsonnes(mot_user1)


#EXO 5
#Question A
def palindrome(mot):
    if(mot==mot[::-1]):
        return True
    else:
        return False

#Question B
def compter(ph1,ph2):
    cpt=0
    for i in range(0,len(ph2)-len(ph1)):
        if ph2[i:len(ph1)+i]==ph1:
            cpt=cpt+1
    return cpt


#question C
def minuscules(phrase):
    l=[]
    for i in phrase:
        if (65<=ord(i)<=90):
            l.append(chr(ord(i)+32))
        else:
            l.append(i)
    resu=""
    for i in l:
        resu=resu+i
    return resu

#Question D
def anagramme(str1,str2):
    if(len(str1)==len(str2)):
        string1=minuscules(str1)
        string2=minuscules(str2)
        if (sorted(string1)==sorted(string2)):
            return True
        else:
            return False
    else:
        return False

#Question E    
def nombre_ident(phr1,phr2):
	lettres_communes = [lettre for lettre in phr1 if lettre in phr2]
	print(lettres_communes)
	lettres_communes_uniques = []

	for lettre in lettres_communes:
		if lettre not in lettres_communes_uniques:
			lettres_communes_uniques.append(lettre)
	return len(lettres_communes_uniques)

def progPrincipal():
#    m=input("Entrez un mot\n")
#    m=m.lower()
#    var=palindrome(m)
#    if(var == True):
#        print(m, " est un palindrome")
#    else:
#        print(m, " n'est pas un palindrome")
#    phr2="Bonjour tout le monde"
#    phr1="on"
#    print("On trouve ",compter(phr1,phr2), " fois " , phr1 ," dans ",phr2)
#    phr3="Bonjour Tout Le Monde"
#    print(minuscules(phr3))
#    if(anagramme("phrAse","eSraPh")):
#        print("c'est un anagramme")
#    else:
#        print("ce n'est pas un anagramme")
    phrase1="abcdef"
    phrase2="aabfghi"
    print("le nombre de lettres communs aux deux phrases est : ",nombre_ident(phrase1,phrase2))

progPrincipal()


# EXO 6
#question A
l=[12,3,5,78,23,11,17,67,54,90,1,14,8,34]
l1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
l3=[1,2,3,1,3,4,5,3,6,5,7,9,2,8,9]

#question A
def moyenne(liste):
    nbr=0
    for i in liste:
        nbr=nbr+i
    nbr=nbr/len(liste)
    return(nbr)

#Question B
def additionListe(liste1,liste2):
    resuListe=[]
    for i in range(0,len(liste1)):
        resuListe.append(liste1[i]+liste2[i])
    return resuListe

#Question C
def listeSansDoublon(liste):
    listeResu=[]
    for i in liste:
        if i not in listeResu:
            listeResu.append(i)
    return listeResu

#Question D
def communsListe(liste1,liste2):
    listeResu=[]
    for i in liste1:
        if i in liste2:
            listeResu.append(i)
    listeResu=listeSansDoublon(listeResu) # si sans doublons
    return listeResu

#Question E
def elementsDistincts(liste1,liste2):
    listeResu=[]
    for i in liste1:
                listeResu.append(i)
    listeResu=listeSansDoublon(listeResu)
    return listeResu


#print(moyenne(l))
#liste=additionListe(l,l1)
#print(liste)
#print(listeSansDoublon(l3))
#print(communsListe(l1,l3))
print(elementsDistincts(l1,l3))
#print(l, "    ",l1)