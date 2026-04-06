while True:
    nom = input("Entre ton nom: ")
    
    if 8 <= len(nom) <= 12:
        print("Bonjour,", nom, "!")
        break
    else:
        print("Le nom doit contenir entre 8 et 12 caractères.")