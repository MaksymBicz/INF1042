liste_a = ["Batterie", "Basse", "Piano", "Basse", "Guitare", "Batterie"]
liste_b = ["Piano", "Voix", "Guitare", "Synthé", "Piano"]

set_a = set(liste_a)
set_b = set(liste_b)

print("Unique A :", set_a)
print("Unique B :", set_b)

print("En commun :", set_a & set_b)

print("Différence :", set_a ^ set_b)

print("Tous uniques :", set_a | set_b)