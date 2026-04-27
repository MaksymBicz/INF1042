import random

A = {random.randint(1, 20) for _ in range(10)}
B = {random.randint(1, 20) for _ in range(10)}

print("A :", A)
print("B :", B)

print("Union :", A | B)
print("Intersection :", A & B)
print("Différence A - B :", A - B)