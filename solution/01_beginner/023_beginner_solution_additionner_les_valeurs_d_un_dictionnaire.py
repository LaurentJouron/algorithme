employes = {"Pierre": 2500, "Marie": 5000, "Julien": 1200}
print(sum(employes.values()))

"""
023 - Additionner les valeurs d'un dictionnaire

SOLUTION :
    employes = {"Pierre": 2500, "Marie": 5000, "Julien": 1200}
    print(sum(employes.values()))

EXPLICATION:
    Encore une fois un exercice assez simple pour qui connait bien Python.
    Pour récupérer toutes les valeurs d'un dictionnaire, on peut utiliser la 
    méthode values :

    >>> employes.values()
    dict_values([2500, 5000, 1200])
    Et pour obtenir la somme de toutes ces valeurs, rien de plus simple que 
    d'utiliser la fonction sum :
    >>> sum(employes.values())
    8700

POINTS IMPORTANTS À RETENIR:
    Pour récupérer toutes les valeurs d'un dictionnaire, on utilise la méthode
    values.
    Pour faire la somme de plusieurs nombres, on utilise la fonction sum.
"""