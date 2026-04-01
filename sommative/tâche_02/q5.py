# Nom: Maksym Bicz
# Jeu pierre, papier, ciseaux contre l'ordinateur.

import random

gagne = 0
perdu = 0

while True:
    choix = input("pierre, papier ou ciseaux: ")
    ordi = random.choice(["pierre", "papier", "ciseaux"])

    print("Ordinateur:", ordi)

    if choix == ordi:
        print("Égalité")
    elif (choix == "pierre" and ordi == "ciseaux") or \
         (choix == "papier" and ordi == "pierre") or \
         (choix == "ciseaux" and ordi == "papier"):
        print("Gagné")
        gagne += 1
    else:
        print("Perdu")
        perdu += 1

    print("Score:", gagne, "gagné,", perdu, "perdu")

    cont = input("Continuer? (oui/non): ")
    if cont != "oui":
        break