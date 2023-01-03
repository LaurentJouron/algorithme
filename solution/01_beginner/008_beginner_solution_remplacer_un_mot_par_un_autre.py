phrase = "Bonjour tout le monde."
nouvelle_phrase = phrase.replace("Bonjour", "Bonsoir")
print(nouvelle_phrase)


"""
008 - Remplacer un mot par un autre - Solution

SOLUTION:
    phrase = "Bonjour tout le monde."
    nouvelle_phrase = phrase.replace("Bonjour", "Bonsoir")
    print(nouvelle_phrase)

EXPLICATION:
    Pour remplacer un mot par un autre en Python on utilise la fonction replace.    
    Le premier argument est le mot à chercher et le second contient ce par quoi
    on veut le remplacer.
    La fonction replace va remplacer toutes les instances de la chaîne de 
    caractère qu'elle trouve dans la phrase. Si vous avez 3 fois le mot 
    "Bonjour", les trois occurrences du mot seront remplacées.

POINTS IMPORTANTS À RETENIR:
    Pour remplacer un mot par un autre on utilise la fonction replace.
"""