# user_registration.py — Sistem de înregistrare utilizatori

"""
User Registration Module (Modul de înregistrare utilizatori)

Colectează datele utilizatorului, le validează și afișează
un sumar formatat al înregistrării.
"""

# ── CONSTANTE ──────────────────────────────────────────────────────────────
MIN_VARSTA    = 18
MAX_VARSTA    = 120
MIN_INALTIME  = 0.5    # metri
MAX_INALTIME  = 2.5    # metri


def citeste_date_utilizator():
    """
    Colectează datele de bază ale utilizatorului prin input.

    Returns:
        dict: Dicționar cu datele introduse de utilizator.
    """
    print("=" * 45)
    print("   ÎNREGISTRARE UTILIZATOR NOU")
    print("=" * 45)

    nume    = input("Nume complet: ")
    email   = input("Adresă email: ")
    varsta  = int(input("Vârsta (ani): "))
    inaltime = float(input("Înălțimea (metri, ex: 1.75): "))

    return {
        "nume": nume,
        "email": email,
        "varsta": varsta,
        "inaltime": inaltime
    }


def afiseaza_sumar(date):
    """
    Afișează un sumar formatat al datelor utilizatorului.

    Args:
        date (dict): Datele utilizatorului colectate prin input.

    Returns:
        None: Funcția nu returnează nimic.
    """
    este_major   = date["varsta"] >= MIN_VARSTA
    varsta_valida = MIN_VARSTA <= date["varsta"] <= MAX_VARSTA
    inaltime_valida = MIN_INALTIME <= date["inaltime"] <= MAX_INALTIME
    date_valide  = varsta_valida and inaltime_valida

    print("\n" + "=" * 45)
    print("   SUMAR ÎNREGISTRARE")
    print("=" * 45)
    print(f"{'Nume:':<15} {date['nume']}")
    print(f"{'Email:':<15} {date['email']}")
    print(f"{'Vârsta:':<15} {date['varsta']} ani")
    print(f"{'Înălțimea:':<15} {date['inaltime']:.2f} m")
    print(f"{'Major:':<15} {'Da' if este_major else 'Nu'}")
    print(f"{'Date valide:':<15} {'Da ✅' if date_valide else 'Nu ❌'}")
    print("=" * 45)


if __name__ == "__main__":
    date = citeste_date_utilizator()
    afiseaza_sumar(date)
# ```
#
# **Output (exemplu cu input: Bogdan, bogdan@mail.com, 42, 1.78):**
# ```
# =============================================
#    ÎNREGISTRARE UTILIZATOR NOU
# =============================================
# Nume complet: Bogdan
# Adresă email: bogdan@mail.com
# Vârsta (ani): 42
# Înălțimea (metri, ex: 1.75): 1.78
#
# =============================================
#    SUMAR ÎNREGISTRARE
# =============================================
# Nume:           Bogdan
# Email:          bogdan@mail.com
# Vârsta:         42 ani
# Înălțimea:      1.78 m
# Major:          Da
# Date valide:    Da ✅
# =============================================