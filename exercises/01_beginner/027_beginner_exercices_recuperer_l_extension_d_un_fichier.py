"""
027 - Récupérer l'extension d'un fichier

Notions abordées : le module os.
    Le but de cet exercice est de récupérer l'extension d'un fichier à l'aide du
    module os.
    Dans ce cas-ci, vous devez récupérer l'extension du fichier python.exe.
    Votre script doit retourner l'extension sans le point. Vous devez donc
    récupérer la chaîne de caractères 'exe'.

Astuces : Pour récupérer l'extension d'un fichier, vous pouvez utiliser la
    fonction os.path.splitext du module os.
"""
import os

fichier = "C:/Python36/python.exe"
