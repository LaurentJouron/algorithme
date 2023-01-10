liste_nombre_pairs = range(2, 101, 2)
print(list(liste_nombre_pairs))

"""
013 - Créer une liste de nombres pairs de 1 à 100 - Solution

SOLUTION:
    liste_nombre_pairs = range(2, 101, 2)
    print(list(liste_nombre_pairs))

EXPLICATION:
    Dans cet exercice, on pousse un peu plus loin encore la fonction range, en
    fournissant un troisième argument, qui va indiquer à la fonction range 
    l'écart que l'on veut entre chaque nombre.
    Dans cet exemple-ci, on indique un écart de 2, ce qui aura comme effet de ne
    pas inclure les nombres impairs dans notre liste (puisque l'on commence à 2).
    Un dernier point auquel il fallait faire attention là encore : pour intégrer
    le nombre 100 dans la liste, il fallait indiquer 101 comme deuxième argument,
    car la fonction range s'arrête à n - 1.

POINTS IMPORTANTS À RETENIR:
    On peut spécifier un écart à la fonction range en passant un nombre en 
    troisième argument.
"""