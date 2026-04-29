
eleves = [
    {"nom": "Ava", "niveau": 12, "activites": ["programmation", "robotique", "mathématiques"]},
    {"nom": "Liam", "niveau": 11, "activites": ["robotique"]},
    {"nom": "Emma", "niveau": 12, "activites": ["art", "mathématiques"]},
    {"nom": "Noah", "niveau": 10, "activites": ["sport", "programmation"]}
]
for e in eleves:
    print(e["nom"])

for e in eleves:
    if e["niveau"] == 12:
        print("12e année :", e["nom"])

activites = set()
for e in eleves:
    activites.update(e["activites"])

print("Activités uniques :", activites)

max_eleve = max(eleves, key=lambda e: len(e["activites"]))
print("Plus actif :", max_eleve["nom"])

count = sum(1 for e in eleves if "robotique" in e["activites"])
print("Nombre en robotique :", count)