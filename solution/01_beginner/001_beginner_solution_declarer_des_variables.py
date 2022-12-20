prenom = "Pierre"
age = 20
majeur = True
compte_en_banque = 20135.384
amis = ["Marie", "Julien", "Adrien"]
parents = ("Marc", "Caroline")

print(prenom)
print(age)
print(majeur)
print(compte_en_banque)
print(amis)
print(parents)

"""
001 - Déclarer des variables - Solution

CODE:
    prenom = "Pierre"
    age = 20
    majeur = True
    compte_en_banque = 20135.384
    amis = ["Marie", "Julien", "Adrien"]
    parents = ("Marc", "Caroline")
     
    print(prenom)
    print(age)
    print(majeur)
    print(compte_en_banque)
    print(amis)
    print(parents)
    
EXPLICATION:
    Dans cet exercice, il suffisait de déclarer les différents types de 
    variable demandés.

POINTS IMPORTANTS À RETENIR:
    - Une chaîne de caractère doit être entourée de deux guillemets.
      Les guillemets peuvent être simples (') ou doubles ("). Vous ne pouvez 
      pas commencer avec des guillemets simples et finir avec des guillemets 
      doubles et vice-versa.
    - Un booléen commence par une majuscule et peut contenir deux valeurs,
      True ou False.
    Si vous essayez de créer un booléen en écrivant true ou false vous 
    obtiendrez une erreur de syntaxe.
    - Pour définir un nombre décimal, on utilise le point (.) et non pas la
      virgule.
    La virgule sert à séparer les éléments les uns des autres.
    Si vous essayez de créer un nombre à virgule avec une virgule au lieu 
    d'un point, vous vous retrouverez avec un tuple contenant les deux nombres 
    de chaque côté de la virgule.

Voyez plutôt :
    nombre = 123,456
    >>> (123, 456)
    nombre = 123.456
    >>> 123.456
    - Pour définir une liste, on utilise les crochets : [ ]
    - Pour définir un tuple, on utilise les parenthèses : ( )
"""