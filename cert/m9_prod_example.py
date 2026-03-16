# inventory.py — Sistem de inventar

"""
Inventory Management Module

Gestionează un inventar de produse folosind dicționar,
cu operații de adăugare, căutare, și raport.
"""

# ── CONSTANTE ──────────────────────────────────────────────────────────────
CATEGORII_VALIDE = ("electronice", "alimentare", "imbracaminte", "altele")


def adauga_produs(inventar, cod, nume, pret, cantitate, categorie):
    """
    Adaugă sau actualizează un produs în inventar.

    Args:
        inventar (dict): Inventarul curent.
        cod (str): Codul unic al produsului.
        nume (str): Numele produsului.
        pret (float): Prețul unitar.
        cantitate (int): Cantitatea în stoc.
        categorie (str): Categoria produsului.

    Returns:
        bool: True dacă adăugat cu succes, False dacă categoria e invalidă.
    """
    if categorie not in CATEGORII_VALIDE:
        return False
    inventar[cod] = {
        "nume":      nume,
        "pret":      pret,
        "cantitate": cantitate,
        "categorie": categorie,
    }
    return True


def cauta_produs(inventar, cod):
    """
    Caută un produs după cod.

    Args:
        inventar (dict): Inventarul curent.
        cod (str): Codul produsului.

    Returns:
        dict | None: Datele produsului sau None dacă nu există.
    """
    return inventar.get(cod)


def raport_inventar(inventar):
    """
    Afișează raportul complet al inventarului.

    Args:
        inventar (dict): Inventarul curent.

    Returns:
        None
    """
    if not inventar:
        print("Inventarul este gol.")
        return

    valoare_totala = sum(
        p["pret"] * p["cantitate"] for p in inventar.values()
    )
    categorii_unice = set(p["categorie"] for p in inventar.values())

    print("=" * 50)
    print(f"  RAPORT INVENTAR — {len(inventar)} produse")
    print("=" * 50)
    for cod, produs in inventar.items():
        print(f"  [{cod}] {produs['nume']:<20} "
              f"{produs['pret']:>8,.2f} RON  "
              f"x{produs['cantitate']}")
    print("-" * 50)
    print(f"  Valoare totală: {valoare_totala:,.2f} RON")
    print(f"  Categorii:      {', '.join(sorted(categorii_unice))}")
    print("=" * 50)


if __name__ == "__main__":
    inventar = {}

    adauga_produs(inventar, "P001", "Laptop",   4999.99, 10, "electronice")
    adauga_produs(inventar, "P002", "Tricou",     89.99, 50, "imbracaminte")
    adauga_produs(inventar, "P003", "Cafea 1kg",  45.00, 30, "alimentare")

    raport_inventar(inventar)

    produs = cauta_produs(inventar, "P001")
    if produs:
        print(f"\nProdus găsit: {produs['nume']} — {produs['pret']} RON")