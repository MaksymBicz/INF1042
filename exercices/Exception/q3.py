solde = 250.00

try:
    montant = float(input("Montant à retirer : "))

    if montant <= 0:
        raise ValueError("le montant doit être supérieur à zéro.")

    if montant > solde:
        raise ValueError("fonds insuffisants.")

except ValueError as e:
    if "could not convert" in str(e):
        print("Erreur : veuillez entrer un nombre valide.")
    else:
        print("Erreur :", e)

else:
    solde -= montant
    print("Retrait accepté.")
    print("Nouveau solde :", solde, "$")

finally:
    print("Fin de la transaction.")