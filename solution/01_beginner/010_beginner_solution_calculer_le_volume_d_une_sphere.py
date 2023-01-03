import math

rayon = 10.0
volume = (4.0 * math.pi / 3.0) * (rayon ** 3)
print(volume)


"""
010 - Calculer le volume d'une sphère - Solution

SOLUTION:
    import math
    rayon = 10.0
    volume = (4.0 * math.pi / 3.0) * (rayon ** 3)
    print(volume)
    
EXPLICATION:
    Peu de difficulté dans cet exercice, le seul point sur lequel il fallait 
    porter attention était l'import du module math, qui permet d'obtenir une 
    valeur précise de pi, sans avoir besoin d'entrer le nombre à la main.
    Le reste est assez simple, le symbole * permet de multiplier, tandis que le
    symbole ** permet de calculer le rayon puissance 3. Le symbole pour la 
    division est la barre oblique (/). Pour obtenir le bon résultat, il fallait
    faire attention également aux parenthèses dans votre calcul.

POINTS IMPORTANTS À RETENIR:
    Pour obtenir la valeur de pi, on importe le module math.
    Pour multiplier, on utilise *, pour mettre le rayon à la puissance 3 on 
    utilise ** et pour diviser on utilise /
"""
