a = 17
b = 5

# Cerinta 2 — Afișează rezultatul tuturor celor 7 operatori aritmetici
print(f"Rezultatul operatiei '+' este: {a + b}")
print(f"Rezultatul operatiei '-' este: {a - b}")
print(f"Rezultatul operatiei '*' este: {a * b}")
print(f"Rezultatul operatiei '/' este: {a / b}")
print(f"Rezultatul operatiei '//' este: {a // b}")
print(f"Rezultatul operatiei '%' este: {a % b}")
print(f"Rezultatul operatiei '**' este: {a ** b}")

# Cerinta 3 — Verifică dacă a este par sau impar folosind %
if a % 2 == 0:
    print("Variabila a este para")
else:
    print("Variabila a este impara")

# Cerinta 4 — Verifică dacă a este divizibil cu b folosind %
if a % b == 0:
    print("Variabila a este divizibila cu variabila b")
else:
    print("Variabila a NU este divizibila cu variabila b")

# Cerinta 5 — Afișează dacă a // b este în intervalul [1, 5] folosind operatori logici
rezultat_impartire = a // b
if 1 <= rezultat_impartire <= 5:
    print(f"Rezultatul a // b ({rezultat_impartire}) se afla in intervalul [1,5]")
else:
    print(f"Rezultatul a // b ({rezultat_impartire}) nu se afla in intervalul [1,5]")
