import random

print("RUNNING...")

with open("valeurs.txt", "w") as f:
    for _ in range(1000):
        f.write(str(random.randint(0, 100000)) + "\n")

print("DONE")