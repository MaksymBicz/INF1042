# Nom: Maksym Bicz
# Ce programme calcule une facture avec rabais et taxe.

prix = float(input("Prix d'achat: "))

if prix < 50:
    rabais = 0
elif prix <= 100:
    rabais = 0.10
else:
    rabais = 0.15

sous_total = prix * (1 - rabais)
taxe = sous_total * 0.13
total = sous_total + taxe

print("Sous-total:", sous_total)
print("Taxe:", taxe)
print("Total:", total)