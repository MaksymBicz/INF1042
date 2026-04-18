with open("valeurs.txt", "r") as f, \
     open("bas.txt", "w") as bas, \
     open("haut.txt", "w") as haut:

    for ligne in f:
        ligne = ligne.strip()

        if ligne != "":
            nombre = int(ligne)

            if 0 <= nombre <= 49999:
                bas.write(str(nombre) + "\n")
            elif 50000 <= nombre <= 100000:
                haut.write(str(nombre) + "\n")

print("bas.txt et haut.txt créés")