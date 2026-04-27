import random

# liste avec doublons
liste = [random.randint(1, 20) for _ in range(100)]
print("Liste originale :", liste)

# enlever doublons avec set
sans_doublons = set(liste)

# transformer en liste triée
liste_triee = sorted(list(sans_doublons))

print("Liste sans doublons triée :", liste_triee)