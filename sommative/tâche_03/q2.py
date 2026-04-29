
produit1 = ("Clavier", 49.99, 12)
produit2 = ("Souris", 29.99, 20)
produit3 = ("Écran", 199.99, 5)


produits = [produit1, produit2, produit3]


for p in produits:
    print("Nom :", p[0])
    print("Prix :", p[1])
    print("Quantité :", p[2])
    print("-----")


for p in produits:
    nom, prix, quantite = p
    print(f"Le produit {nom} coûte {prix} $ et il y en a {quantite} en stock.")


produit_plus_cher = produits[0]

for p in produits:
    if p[1] > produit_plus_cher[1]:
        produit_plus_cher = p

print("Produit le plus cher :", produit_plus_cher[0], "-", produit_plus_cher[1], "$")