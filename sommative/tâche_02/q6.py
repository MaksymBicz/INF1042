# Nom: Maksym Bicz
# Ce programme calcule les frais de stationnement.

heures = int(input("Nombre d'heures: "))
electrique = input("Voiture électrique? (oui/non): ")

cout = 4

if heures > 1:
    cout += (heures - 1) * 3

if heures > 5:
    cout += 10

if electrique == "oui":
    cout *= 0.8

print("Coût total:", cout)