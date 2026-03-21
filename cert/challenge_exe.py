"""
PCEP Certification — Challenge Exercises
Toate exercițiile provocare din modulele 1.5 → 3.2
"""


# ══════════════════════════════════════════════════════════════════════════════
# MODUL 1.5 — Input/Output și String Formatting
# ══════════════════════════════════════════════════════════════════════════════
# Cerință:
# Citește de la utilizator: nume, nota (float), materie.
# Afișează:
#   1. Nota cu 2 zecimale
#   2. Nota ca procent din 10 (:.1%)
#   3. Status: "Promovat" dacă nota >= 5, altfel "Picat"
#   4. Separator de 35 de caractere "="

def colecteaza_date():
    """
    Colectează datele de bază ale utilizatorului prin input.

    Returns:
        dict: Dicționar cu datele introduse de utilizator.
    """
    nume    = input("Introdu numele: ")
    nota    = float(input("Introdu nota: "))
    materie = input("Introdu materia: ")
    return {"nume": nume, "nota": nota, "materie": materie}


def rezolva_cerinte():
    """
    Afișează rezultatele formatate conform cerințelor.

    Returns:
        None
    """
    values = colecteaza_date()
    print(f"{values['nota']:.2f}")
    print(f"{values['nota'] / 10:.1%}")
    print(f"{'Promovat' if values['nota'] >= 5 else 'Picat'}")
    print("=" * 35)


# ══════════════════════════════════════════════════════════════════════════════
# MODUL 2.1 — Control Flow: if / elif / else
# ══════════════════════════════════════════════════════════════════════════════
# Cerință:
# Citește de la utilizator un număr întreg n.
# Afișează dacă n este:
#   1. Pozitiv par / Pozitiv impar / Negativ par / Negativ impar / Zero
#   2. Dacă n este divizibil cu 3, cu 5, sau cu ambele (FizzBuzz)
#   3. Folosește cel puțin o condiție compusă cu "and"

def clasificare_numar():
    """
    Citește un număr întreg și îl clasifică după semn, paritate și FizzBuzz.

    Returns:
        None
    """
    n = int(input("Introdu un număr întreg: "))

    if n == 0:
        print("Zero")
    elif n > 0 and n % 2 == 0:
        print("Pozitiv par")
    elif n > 0 and n % 2 != 0:
        print("Pozitiv impar")
    elif n < 0 and n % 2 == 0:
        print("Negativ par")
    else:
        print("Negativ impar")

    if n % 3 == 0 and n % 5 == 0:
        print("Divizibil cu 3 și cu 5 (FizzBuzz!)")
    elif n % 3 == 0:
        print("Divizibil cu 3 (Fizz)")
    elif n % 5 == 0:
        print("Divizibil cu 5 (Buzz)")
    else:
        print("Nu este divizibil nici cu 3, nici cu 5")


# ══════════════════════════════════════════════════════════════════════════════
# MODUL 2.2 — Loops: while și for
# ══════════════════════════════════════════════════════════════════════════════
# Cerință:
#   1. Folosind for și range(), calculează suma tuturor numerelor de la 1 la 100
#   2. Folosind while, găsește primul număr din [1, 1000] divizibil cu 7 și cu 11
#   3. Folosind for cu break și else, verifică dacă numărul 97 este prim
#   4. Afișează rezultatele clar formatate

def exercitiu_loops():
    """
    Demonstrează utilizarea for, while, break și else în loop-uri.

    Returns:
        None
    """
    # Cerinta 1 — suma 1-100 cu for
    suma = 0
    for i in range(1, 101):
        suma += i
    print(f"Suma numerelor de la 1 la 100 este {suma}")

    # Cerinta 2 — primul divizibil cu 7 și 11 cu while
    i = 1
    while i <= 1000:
        if i % 7 == 0 and i % 11 == 0:
            print(f"Primul numar din intervalul [1, 1000] divizibil cu 7 și 11: {i}")
            break
        i += 1

    # Cerinta 3 — verificare număr prim cu for/else/break
    number = 97
    for i in range(2, number):
        if number % i == 0:
            print(f"Numarul {number} nu este prim, este divizibil cu {i}!")
            break
    else:
        print(f"Numarul {number} este prim!")


# ══════════════════════════════════════════════════════════════════════════════
# MODUL 3.1 — Lists (Liste)
# ══════════════════════════════════════════════════════════════════════════════
# Cerință:
#   1. Creează o listă cu 5 numere introduse de utilizator cu input()
#   2. Afișează: suma, media, min, max
#   3. Afișează lista sortată crescător și descrescător
#   4. Șterge toate elementele mai mici decât media și afișează lista rezultată
#   5. Folosește cel puțin: append(), sorted(), del

def exercitiu_liste():
    """
    Colectează 5 numere și efectuează operații de statistică și filtrare.

    Returns:
        None
    """
    numere = []
    for i in range(5):
        numere.append(int(input(f"Numărul {i + 1}: ")))

    print(f"Suma numerelor din lista este {sum(numere)}")
    print(f"Media numerelor din lista este {sum(numere) / len(numere):.2f}")
    print(f"Minim din lista este {min(numere)}")
    print(f"Maximum din lista este {max(numere)}")
    print(f"Lista sortata crescator este {sorted(numere)}")
    print(f"Lista sortata descrescator este {sorted(numere, reverse=True)}")

    media = sum(numere) / len(numere)           # calculat O SINGURĂ DATĂ!
    for i in range(len(numere) - 1, -1, -1):   # iterare inversă
        if numere[i] < media:
            del numere[i]                        # del după index — precis cu duplicate
    print(f"Lista dupa stergerea elementelor sub medie: {numere}")


# ══════════════════════════════════════════════════════════════════════════════
# MODUL 3.2 — Tuples, Dictionaries, Sets
# ══════════════════════════════════════════════════════════════════════════════
# Cerință:
#   1. Creează un dicționar cu 3 studenți — cheia = nume, valoarea = listă de 3 note
#   2. Calculează și afișează media fiecărui student
#   3. Afișează studentul cu cea mai mare medie
#   4. Folosind un set, afișează câte note distincte există în total
#   5. Stochează datele fiecărui student ca tuple (medie, status)
#      unde status = "Promovat" dacă media >= 5, altfel "Picat"

def exercitiu_colectii():
    """
    Demonstrează utilizarea dicționarelor, seturilor și tuple-urilor.

    Returns:
        None
    """
    # Cerinta 1 — dicționar cu 3 studenți
    students = {
        "Bogdan": [10, 8, 10],
        "Sofia":  [10, 10, 10],
        "Milena": [9, 10, 10],
    }

    # Cerinta 2 — media fiecărui student
    condensedStudents = {}
    for key, notes in students.items():
        average = sum(notes) / len(notes)
        print(f"Media studentului {key} este: {average:.2f}")
        condensedStudents[key] = average

    # Cerinta 3 — studentul cu cea mai mare medie
    top_student = max(condensedStudents, key=condensedStudents.get)
    print(f"Studentul cu cea mai mare medie: {top_student} — {condensedStudents[top_student]:.2f}")

    # Cerinta 4 — note distincte cu set
    grades = set()
    for key, notes in students.items():
        grades.update(notes)
    print(f"Totalitatea notelor distincte este: {len(grades)}")

    # Cerinta 5 — tuple (medie, status) per student
    for key, value in condensedStudents.items():
        status = "Promovat" if value >= 5 else "Picat"
        stud = (value, status)
        print(f"{key}: {stud}")


# ══════════════════════════════════════════════════════════════════════════════
# ENTRY POINT
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("  MODUL 1.5 — Input/Output și String Formatting")
    print("=" * 50)
    rezolva_cerinte()

    print("\n" + "=" * 50)
    print("  MODUL 2.1 — Control Flow")
    print("=" * 50)
    clasificare_numar()

    print("\n" + "=" * 50)
    print("  MODUL 2.2 — Loops")
    print("=" * 50)
    exercitiu_loops()

    print("\n" + "=" * 50)
    print("  MODUL 3.1 — Liste")
    print("=" * 50)
    exercitiu_liste()

    print("\n" + "=" * 50)
    print("  MODUL 3.2 — Tuples, Dictionaries, Sets")
    print("=" * 50)
    exercitiu_colectii()
