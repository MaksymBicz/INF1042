while True:
    try:
        a = float(input("Entre la première valeur: "))
        b = float(input("Entre la deuxième valeur: "))
        
        print("Produit:", a * b)
        print("Différence:", a - b)
        break
    except:
        print("Veuillez entrer des nombres valides (float).")