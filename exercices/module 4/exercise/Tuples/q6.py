matchs = (
    ("Tigres", "Lynx", 25, 18),
    ("Aigles", "Panthères", 22, 25),
    ("Tigres", "Panthères", 25, 23),
    ("Lynx", "Aigles", 19, 25),
    ("Tigres", "Aigles", 21, 25),
    ("Lynx", "Panthères", 25, 20)
)

victoires = {}
points = {}

for eq1, eq2, s1, s2 in matchs:
    # ajouter points
    points[eq1] = points.get(eq1, 0) + s1
    points[eq2] = points.get(eq2, 0) + s2

    # déterminer gagnant
    if s1 > s2:
        print(f"Les {eq1} ont battu les {eq2} {s1}-{s2}")
        victoires[eq1] = victoires.get(eq1, 0) + 1
    else:
        print(f"Les {eq2} ont battu les {eq1} {s2}-{s1}")
        victoires[eq2] = victoires.get(eq2, 0) + 1

print("\nVictoires:", victoires)
print("Meilleure équipe:", max(victoires, key=victoires.get))

print("\nPoints:", points)
print("Plus de points:", max(points, key=points.get))