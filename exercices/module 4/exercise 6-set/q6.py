import random

eleves = {"Maksym", "Léo", "Hayden", "Angel", "Ibrahim", "Josh", "Grant", "Maxime", "David"}

eleves = list(eleves)

random.shuffle(eleves)

for e in eleves:
    print(e)