import random

mot = "Bonjour"
mot = list(mot)

random.shuffle(mot)

mot_random = "".join(mot).capitalize()
print(mot_random)

"""
033 - Mélanger les lettres d'un mot

SOLUTION:
    import random
    mot = "Bonjour"
    mot = list(mot)
    random.shuffle(mot)
    mot_random = "".join(mot).capitalize()
    print(mot_random)
    
EXPLICATION:
    Pour facilement mélanger les lettres d'un mot, nous allons utiliser le 
    module random et la fonction shuffle.
    La fonction shuffle fonctionne sur des listes et permet de mélanger les 
    éléments de la liste qui lui est passée.
    Nous allons donc commencer par convertir notre mot en liste avec la 
    fonction list :
    mot = list(mot)
    Nous utilisons ensuite la fonction shuffle du module random pour mélanger
    la liste :
    random.shuffle(mot)
    Il ne reste plus qu'à rassembler tous les éléments de la liste avec la 
    fonction join et de remettre la majuscule à la bonne place avec la 
    fonction capitalize :
    mot_random = "".join(mot).capitalize()
    
POINTS IMPORTANTS À RETENIR
    Pour mélanger les éléments d'une liste, on utilise la fonction shuffle du 
    module random.
    Pour convertir une chaîne de caractères en liste, on utilise la fonction 
    list.
"""