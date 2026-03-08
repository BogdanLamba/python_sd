# bmi_calculator.py — Calculator BMI (Body Mass Index)

"""
BMI Calculator Module (Modul calculator indice de masă corporală)

Calculează și interpretează indicele de masă corporală (IMC/BMI)
pe baza greutății și înălțimii introduse de utilizator.
"""

# ── CONSTANTE ──────────────────────────────────────────────────────────────
BMI_SUBPONDERAL  = 18.5
BMI_NORMAL       = 25.0
BMI_SUPRAPONDERAL = 30.0


def calculeaza_bmi(greutate, inaltime):
    """
    Calculează indicele de masă corporală.

    Args:
        greutate (float): Greutatea în kilograme.
        inaltime (float): Înălțimea în metri.

    Returns:
        float | None: Valoarea BMI sau None dacă datele sunt invalide.
    """
    if greutate <= 0 or inaltime <= 0:
        return None
    return greutate / (inaltime ** 2)


def interpreteaza_bmi(bmi):
    """
    Interpretează valoarea BMI și returnează categoria.

    Args:
        bmi (float): Valoarea BMI calculată.

    Returns:
        str: Categoria de greutate.
    """
    if bmi < BMI_SUBPONDERAL:
        return "Subponderal"
    elif bmi < BMI_NORMAL:
        return "Greutate normală ✅"
    elif bmi < BMI_SUPRAPONDERAL:
        return "Supraponderal"
    else:
        return "Obezitate"


def afiseaza_rezultat(nume, bmi, categorie):
    """
    Afișează rezultatul formatat al calculului BMI.

    Args:
        nume (str): Numele utilizatorului.
        bmi (float): Valoarea BMI.
        categorie (str): Categoria de greutate.

    Returns:
        None
    """
    print("=" * 40)
    print(f"  Rezultat BMI — {nume}")
    print("=" * 40)
    print(f"  BMI:      {bmi:.2f}")
    print(f"  Categorie: {categorie}")
    print("=" * 40)


if __name__ == "__main__":
    print("=== Calculator BMI ===\n")

    nume     = input("Nume: ")
    greutate = float(input("Greutate (kg): "))
    inaltime = float(input("Înălțime (m): "))

    bmi = calculeaza_bmi(greutate, inaltime)

    if bmi is None:
        print("Date invalide — greutatea și înălțimea trebuie să fie pozitive!")
    else:
        categorie = interpreteaza_bmi(bmi)
        afiseaza_rezultat(nume, bmi, categorie)