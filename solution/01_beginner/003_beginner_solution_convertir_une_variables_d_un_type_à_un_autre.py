nombre = 15
print("Le nombre est " + str(nombre))


"""
003 - Convertir une variable d'un type à un autre - Solution

SOLUTION:
    nombre = 15
    print("Le nombre est " + str(nombre))

EXPLICATION:
    Là encore un exercice très simple pour ceux qui sont habitués à Python.
    Dans Python, on ne peut pas concaténer des variables de différents types. 
    Ainsi, si on essaie d'additionner une chaîne de caractères avec un nombre, 
    on se retrouve avec une erreur :
    >>> nombre = 15
    >>> print("Le nombre est " + nombre)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: must be str, not int
    L'erreur ci-dessus nous indique que le type de la variable 'nombre', 
    pour être concaténé avec la chaîne de caractère 'Le nombre est ', doit être
    de type 'str' (chaîne de caractère) et non pas 'int' (nombre entier).
    Pour remédier à ce problème, on convertit donc notre nombre 15, par la
    chaîne de caractère '15', grâce à la fonction str.

POINTS IMPORTANTS À RETENIR:
    - Pour convertir un nombre en chaîne de caractère, on utilise la fonction str.
    - Pour convertir une chaîne de caractère en nombre, on utilise la fonction int.
    Attention : si vous essayez de convertir une chaîne de caractère qui ne 
    contient pas un nombre en 'integer' avec la fonction int, vous aurez une 
    erreur:
    >>> int("Udemy")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: invalid literal for int() with base 10: 'Udemy'
    Pour vérifier si une chaîne de caractère ne contient que des chiffres, 
    vous pouvez utiliser la méthode isdigit :
    >>> "Udemy".isdigit()
    False
    >>> "2018".isdigit()
    True
    >>>
"""