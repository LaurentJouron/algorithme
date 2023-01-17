from time import time

a = time()
_ = [i*2 for i in range(9999999)]
print(f"Temps d'exécution: {time() - a} secondes")

"""
    On stock dans la variable "a" l'heure exact du début du script.
    On récupère l'heure de la fin à laquelle on la soustrait à "a", ce qui donne
    le temps d'exécution.  
"""
