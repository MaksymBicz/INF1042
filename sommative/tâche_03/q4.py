#  Dictionnaire
inventaire = {
    "stylos": 24,
    "cahiers": 15,
    "gommes": 10
}

print("Cahiers :", inventaire["cahiers"])

inventaire["marqueurs"] = 18

inventaire["stylos"] = 30

del inventaire["gommes"]

for produit, quantite in inventaire.items():
    print(produit, ":", quantite)


total = sum(inventaire.values())
print("Total articles :", total)