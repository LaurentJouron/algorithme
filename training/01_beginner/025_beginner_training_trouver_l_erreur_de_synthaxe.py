"""
025 - Trouver l'erreur de syntaxe

Notions abordées : syntaxe.
    On continue avec les erreurs et la syntaxe. Le script suivant ne fonctionne
    pas, à vous de trouver pourquoi et de le corriger.
    Votre script doit retourner la liste [2, 6, 12, 20, 42, 56, 90] .

Astuces : Comptez bien le nombre de parenthèses et de crochets. Il doit y en avoir
    le même nombre dans un sens que dans l'autre !
"""

liste = [1, 1, 4, 3, 3, 2, 6, 7, 7, 9, 2]

resultat = [i*(i+1%(i*5) for i in sorted(list(set(liste))]
print(resultat)
