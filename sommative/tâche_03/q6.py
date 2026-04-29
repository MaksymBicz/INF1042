achats = [
    ("Liam", "Galaxy Battle", "PC", 59.99),
    ("Emma", "Speed Zone", "PlayStation", 49.99),
    ("Liam", "Pixel Quest", "Switch", 39.99),
    ("Noah", "Galaxy Battle", "PC", 59.99),
    ("Emma", "Sky Builder", "PC", 29.99),
    ("Olivia", "Speed Zone", "Xbox", 54.99),
    ("Liam", "Sky Builder", "PC", 29.99),
    ("Noah", "Pixel Quest", "Switch", 39.99)
]

print("Liste des achats :")
for nom, jeu, plateforme, prix in achats:
    print(f"{nom} a acheté {jeu} sur {plateforme} pour {prix} $")

jeux_uniques = {a[1] for a in achats}

plateformes_uniques = {a[2] for a in achats}

montant_total = sum(a[3] for a in achats)
print("\nMontant total dépensé :", montant_total, "$")

depenses = {}
for nom, jeu, plateforme, prix in achats:
    depenses[nom] = depenses.get(nom, 0) + prix

print("\nDépenses par client :")
for client, total in depenses.items():
    print(client, ":", total, "$")

client_max = max(depenses, key=depenses.get)
print("\nClient qui a le plus dépensé :", client_max)

compte_jeux = {}
for nom, jeu, plateforme, prix in achats:
    compte_jeux[jeu] = compte_jeux.get(jeu, 0) + 1

print("\nAchats sur PC :")
for nom, jeu, plateforme, prix in achats:
    if plateforme == "PC":
        print(f"{nom} a acheté {jeu} pour {prix} $")

jeu_plus_achete = max(compte_jeux, key=compte_jeux.get)

print("\n===== RÉSUMÉ =====")
print("Nombre total d’achats :", len(achats))
print("Jeux uniques :", jeux_uniques)
print("Plateformes uniques :", plateformes_uniques)
print("Montant total dépensé :", montant_total, "$")
print("Client qui a le plus dépensé :", client_max)
print("Jeu le plus acheté :", jeu_plus_achete)