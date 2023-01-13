"""
022 - Récupérer une valeur dans un dictionnaire
Notions abordées : les dictionnaires.
    Dans cet exercice, nous allons récupérer la valeur de la clé 'prenom',
    contenue dans le dictionnaire employes.
    Votre script doit donc retourner la chaîne de caractères 'Pierre'.
    Aller plus loin : construisez votre script de sorte qu’il ne produise
    aucune erreur si les clés du dictionnaire venaient à être modifiées.

Astuces : Afin d'éviter le risque d'erreur, utilisez la fonction get, qui vous
    permet de spécifier un élément par défaut à retourner au cas où la clé
    que vous cherchez n'existe pas.
"""

employes = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}
