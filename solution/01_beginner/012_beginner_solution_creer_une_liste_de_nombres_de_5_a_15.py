liste_de_nombres = range(5, 16)
print(list(liste_de_nombres))

"""
012 - Créer une liste de nombres de 5 à 15 - Solution

SOLUTION:
    liste_de_nombres = range(5, 16)
    print(list(liste_de_nombres))
    EXPLICATION
    Pour créer facilement et rapidement des listes de nombres, on utilise la
    fonction range.
    On peut l'utiliser en passant un seul nombre en argument, auquel cas la
    fonction range va créer une liste allant de 0 jusqu'au nombre indiqué - 1 :
    #>>> list(range(10))
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    Vous voyez dans l'exemple ci-dessus, que la liste s'arrête à 9.
    On peut également passer deux arguments, pour indiquer à la fonction à
    partir de quel nombre commencer, comme dans cet exercice :
    #>>> list(range(5, 16))
    [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    Là encore, vous remarquerez que la liste s'arrête à 15. Si nous voulons
    inclure le nombre 15 dans la liste, il faut donc passer en deuxième
    argument le nombre 16.
    Attention ! Depuis Python 3, la fonction range ne retourne pas une liste
    mais un objet de type 'range'.
    Ainsi, si vous voulez afficher cet objet en tant que liste, il vous faudra
    utiliser la fonction list pour convertir l'objet range en liste.

POINTS IMPORTANTS À RETENIR:
    La fonction range permet de générer une liste de nombres rapidement.
    Depuis Python 3, il faut utiliser la fonction list pour convertir le
    résultat de la fonction range en liste.
"""