
notes = [78, 85, 92, 67, 85, 74]

print("Liste des notes :", notes)

print("Première note :", notes[0])
print("Dernière note :", notes[-1])

notes.append(88)

notes.remove(85)

print("Liste mise à jour :", notes)

total = sum(notes)
moyenne = total / len(notes)
note_max = max(notes)
note_min = min(notes)

print("Total :", total)
print("Moyenne :", moyenne)
print("Note max :", note_max)
print("Note min :", note_min)