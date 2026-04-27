texte = """Dans un coin oublié d’un vieux laboratoire, vivait un petit ordinateur gris..."""

# enlever ponctuation
texte = texte.lower()
for p in [",", ".", "!", "?", ":", ";", "’", "'", "«", "»"]:
    texte = texte.replace(p, "")

mots = texte.split()

# dictionnaire
compte = {}

for mot in mots:
    if mot in compte:
        compte[mot] += 1
    else:
        compte[mot] = 1

print(compte)