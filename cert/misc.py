# Citire și conversie
nume   = input("Introdu numele: ")
varsta = int(input("Introdu vârsta: "))

# Calcul cu valoarea convertită
an_nastere = 2026 - varsta - 1

print(f"Bună, {nume}!")
print(f"Ai {varsta} ani și te-ai născut în {an_nastere}.")

if varsta >= 18:
    print("Ești major — ai acces complet.")
else:
    print(f"Ești minor — mai ai {18 - varsta} ani până la majorat.")