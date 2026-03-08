def colecteaza_date():
    nume    = input("Introdu numele: ")
    nota    = float(input("Introdu nota: "))
    materie = input("Introdu materia: ")
    return {"nume": nume, "nota": nota, "materie": materie}


def rezolva_cerinte():
    values = colecteaza_date()
    print(f"{values['nota']:.2f}")
    print(f"{values['nota'] / 10:.1%}")
    print(f"{'Promovat' if values['nota'] >= 5 else 'Picat'}")
    print("=" * 35)


if __name__ == "__main__":
    rezolva_cerinte()
