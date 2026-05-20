try:
    note1 = float(input("Note 1 : "))
    note2 = float(input("Note 2 : "))

    if note1 < 0 or note1 > 100 or note2 < 0 or note2 > 100:
        raise ValueError("les notes doivent être entre 0 et 100.")

except ValueError as e:
    if "could not convert" in str(e):
        print("Erreur : les notes doivent être numériques.")
    else:
        print("Erreur :", e)

else:
    moyenne = (note1 + note2) / 2
    print("La moyenne est :", moyenne)

finally:
    print("Fin du programme.")