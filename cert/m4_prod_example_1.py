# calculator.py — Calculator simplu cu toate tipurile de operatori

"""
Simple Calculator Module (Modul calculator simplu)

Demonstrează utilizarea operatorilor aritmetici, de comparare
și logici într-un context real.
"""


def calculeaza(a, b, operator):
    """
    Efectuează o operație matematică între două numere.

    Args:
        a (float): Primul operand.
        b (float): Al doilea operand.
        operator (str): Operatorul: '+', '-', '*', '/', '//', '%', '**'

    Returns:
        float | None: Rezultatul operației sau None dacă operatorul e invalid.
    """
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        # Împărțirea la 0 nu este permisă matematica
        if b == 0:
            print("Eroare: împărțire la zero!")
            return None
        return a / b
    elif operator == '//':
        if b == 0:
            print("Eroare: împărțire la zero!")
            return None
        return a // b
    elif operator == '%':
        if b == 0:
            print("Eroare: modulo cu zero!")
            return None
        return a % b
    elif operator == '**':
        return a ** b
    else:
        print(f"Operator necunoscut: {operator}")
        return None


def verifica_rezultat(rezultat, minim, maxim):
    """
    Verifică dacă rezultatul se află în intervalul acceptabil.

    Args:
        rezultat (float): Valoarea de verificat.
        minim (float): Limita inferioară a intervalului.
        maxim (float): Limita superioară a intervalului.

    Returns:
        bool: True dacă rezultatul este în interval.
    """
    # Folosim and pentru a verifica ambele condiții simultan
    return rezultat is not None and minim <= rezultat <= maxim


if __name__ == "__main__":
    print("=" * 45)
    print("  Calculator — Demo operatori")
    print("=" * 45)

    operatii = [
        (10, 3, '+'),
        (10, 3, '/'),
        (10, 3, '//'),
        (10, 3, '%'),
        (2, 8, '**'),
        (10, 0, '/'),   # caz special — împărțire la 0
    ]

    for a, b, op in operatii:
        rez = calculeaza(a, b, op)
        if rez is not None:
            in_interval = verifica_rezultat(rez, 0, 100)
            print(f"  {a} {op} {b} = {rez} | în [0,100]: {in_interval}")

    print("=" * 45)

# **Output:**
# ```
# =============================================
#   Calculator — Demo operatori
# =============================================
#   10 + 3 = 13 | în [0,100]: True
#   10 / 3 = 3.3333333333333335 | în [0,100]: True
#   10 // 3 = 3 | în [0,100]: True
#   10 % 3 = 1 | în [0,100]: True
#   2 ** 8 = 256 | în [0,100]: False
# Eroare: împărțire la zero!
# =============================================