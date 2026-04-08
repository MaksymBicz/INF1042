notes = [12, 15, 9, 18, 15, 12]

# moyenne
moyenne = sum(notes) / len(notes)
print("Moyenne:", moyenne)

# valeur la plus fréquente (sans set)
frequent = notes[0]
max_count = 0

for n in notes:
    count = 0
    for x in notes:
        if x == n:
            count += 1
    if count > max_count:
        max_count = count
        frequent = n

print("Valeur la plus fréquente:", frequent)