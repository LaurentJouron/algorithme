ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(ma_liste[::2])

"""
018 - Récupérer un élément sur deux dans une liste

SOLUTION:
    ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(ma_liste[::2])

EXPLICATION:
    Encore une fois, nous utilisons ici le 'slicing' pour récupérer uniquement
    un élément sur deux dans notre liste.
    Nous pouvons indiquer en effet un troisième nombre entre les crochets et ce
    nombre indique le pas avec lequel nous voulons récupérer les éléments de notre
    liste.
    Là encore, pas besoin d'indiquer d'indice spécifique pour les deux premiers
    nombres : en n'indiquant aucun indice, le slicing commencera automatiquement
    au début de la liste, ira jusqu'à la fin, en prenant seulement un élément sur
    deux:
    ma_liste[::2]
    La syntaxe complète du slicing est donc la suivante :
    ma_liste[indice_de_depart:indice_de_fin:pas]
    Si on veut récupérer les éléments de 4 à 25 avec un pas de 3 on fera donc :
    #>>> ma_liste = range(100)
    #>>> ma_liste[4:26:3]
    [4, 7, 10, 13, 16, 19, 22, 25]

POINTS IMPORTANTS À RETENIR:
    Pour récupérer un élément sur deux, on utilise le slicing et on indique un
    pas de 2 à l'intérieur des crochets.
"""