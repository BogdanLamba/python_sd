# gradebook.py — Catalog de note

"""
Gradebook Module

Gestionează notele studenților: adăugare, statistici,
filtrare și raport final.
"""

MIN_NOTA  = 1.0
MAX_NOTA  = 10.0
PRAG_PROM = 5.0


def adauga_nota(note, nota):
    """
    Adaugă o notă validă în catalog.

    Args:
        note (list): Lista curentă de note.
        nota (float): Nota de adăugat.

    Returns:
        bool: True dacă nota a fost adăugată, False dacă e invalidă.
    """
    if not (MIN_NOTA <= nota <= MAX_NOTA):
        return False
    note.append(nota)
    return True


def statistici(note):
    """
    Calculează statisticile unui set de note.

    Args:
        note (list): Lista de note.

    Returns:
        dict: Dicționar cu medie, min, max, nr. promovați.
    """
    if not note:
        return None
    promovate = [n for n in note if n >= PRAG_PROM]
    return {
        "medie":     sum(note) / len(note),
        "maxima":    max(note),
        "minima":    min(note),
        "promovati": len(promovate),
        "picati":    len(note) - len(promovate),
    }


def raport(nume_clasa, note):
    """
    Afișează raportul complet al clasei.

    Args:
        nume_clasa (str): Numele clasei.
        note (list): Lista de note.

    Returns:
        None
    """
    stats = statistici(note)
    if stats is None:
        print("Nu există note înregistrate.")
        return

    print("=" * 40)
    print(f"  Raport — {nume_clasa}")
    print("=" * 40)
    print(f"  Note:       {sorted(note)}")
    print(f"  Medie:      {stats['medie']:.2f}")
    print(f"  Maximă:     {stats['maxima']:.1f}")
    print(f"  Minimă:     {stats['minima']:.1f}")
    print(f"  Promovați:  {stats['promovati']}/{len(note)}")
    print(f"  Picați:     {stats['picati']}/{len(note)}")
    print("=" * 40)


if __name__ == "__main__":
    note_clasa = []
    print("Introdu notele (0 pentru stop):\n")

    while True:
        try:
            nota = float(input("Notă: "))
        except ValueError:
            print("Introdu un număr valid!")
            continue
        if nota == 0:
            break
        if not adauga_nota(note_clasa, nota):
            print(f"Notă invalidă — trebuie între {MIN_NOTA} și {MAX_NOTA}!")

    raport("Clasa 10A", note_clasa)