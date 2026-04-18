with open("valeurs.txt", "r") as f:
    nombres = []

    for ligne in f:
        ligne = ligne.strip()
        if ligne != "":  # évite les lignes vides
            nombres.append(int(ligne))

max_val = max(nombres)
min_val = min(nombres)
moyenne = sum(nombres) / len(nombres)

print("Maximum:", max_val)
print("Minimum:", min_val)
print("Moyenne:", moyenne)