try:
    age = input("Entrez votre âge : ")

    if not age.isdigit():
        raise ValueError("l'âge doit être un nombre entier.")

    age = int(age)

except ValueError as e:
    print("Erreur :", e)

else:
    print("Vous avez", age, "ans.")