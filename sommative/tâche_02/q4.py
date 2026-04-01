# Nom: Maksym Bicz
# Ce programme simule des nombres aléatoires de 1 à 4.

import random

n = int(input("Combien de valeurs? "))

c1 = c2 = c3 = c4 = 0

for i in range(n):
    r = random.randint(1, 4)
    if r == 1:
        c1 += 1
    elif r == 2:
        c2 += 1
    elif r == 3:
        c3 += 1
    else:
        c4 += 1

print("Valeur 1:", c1, "fois", f"({c1/n*100:.1f} %)")
print("Valeur 2:", c2, "fois", f"({c2/n*100:.1f} %)")
print("Valeur 3:", c3, "fois", f"({c3/n*100:.1f} %)")
print("Valeur 4:", c4, "fois", f"({c4/n*100:.1f} %)")