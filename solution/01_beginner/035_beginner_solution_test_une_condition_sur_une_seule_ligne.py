a = 20
majeur = print("Vous êtes majeur !") if a >= 18 else print("Vous êtes mineur")

"""
035 - Tester une condition sur une ligne

SOLUTION:
    a = 20
    majeur = print("Vous êtes majeur !") if a >= 18 else print("Vous êtes mineur")

EXPLICATION:
    Pour résoudre cet exercice, il fallait utiliser ce qu'on appelle un 
    opérateur ternaire.
    De cette façon, nous pouvons réaliser une condition if, else sur une 
    seule ligne.
    Il est important de noter qu'il n'est possible d'inclure des print dans
    un opérateur ternaire que depuis la version 3 de Python.
    À noter aussi, il n'est pas possible d'inclure un elif dans un opérateur
    ternaire.
    Nous n'avons donc que deux choix possibles avec le if et le else, en suivant
    la syntaxe suivante :
    variable = expression if condition else expression 

POINTS IMPORTANTS À RETENIR:
    Pour réaliser une structure conditionnelle sur une seule ligne, on utilise un opérateur ternaire.
"""