# payment_processor.py
# Modul de procesare plăți — exemplu de cod bine structurat și comentat

"""
Payment Processor Module (Modul de procesare plăți)

Gestionează validarea și procesarea plăților pentru platforma e-commerce.
Suportă plăți prin card, transfer bancar și portofele digitale.

Author (Autor): Bogdan
Version (Versiune): 1.0.0
"""

import keyword  # Standard library — verificare keywords
import sys      # Standard library — informații sistem


# ── CONSTANTE ────────────────────────────────────────────────────────────────
# Convențe PEP-8: constantele se scriu cu MAJUSCULE și underscore
MAX_RETRIES = 3          # Număr maxim de reîncercări la eșec
TIMEOUT_SECONDS = 30     # Timeout pentru conexiunea la gateway
MIN_AMOUNT = 0.01        # Suma minimă acceptată în EUR


# ── FUNCȚII PRINCIPALE ────────────────────────────────────────────────────────

def valideaza_suma(suma):
    """
    Validează dacă suma de plată este acceptabilă.

    Args:
        suma (float): Suma de plată în EUR.

    Returns:
        bool: True dacă suma este validă, False altfel.
    """
    # Suma trebuie să fie pozitivă și să depășească minimul acceptat
    if suma <= 0:
        return False

    if suma < MIN_AMOUNT:
        # Sumele sub 1 cent nu sunt procesabile din cauza comisioanelor
        return False

    return True


def proceseaza_plata(suma, metoda):
    """
    Procesează o plată folosind metoda specificată.

    Args:
        suma (float): Suma de plată în EUR.
        metoda (str): Metoda de plată ('card', 'transfer', 'wallet').

    Returns:
        dict: Rezultatul procesării cu status și transaction_id.
    """
    # Pas 1: Validare sumă
    if not valideaza_suma(suma):
        # Returnăm eroare fără să contactăm gateway-ul
        return {
            "status": "error",
            "mesaj": f"Suma {suma} EUR nu este validă",
            "transaction_id": None
        }

    # Pas 2: Verificare metodă de plată
    metode_acceptate = ["card", "transfer", "wallet"]

    if metoda not in metode_acceptate:
        return {
            "status": "error",
            "mesaj": f"Metoda '{metoda}' nu este acceptată",
            "transaction_id": None
        }

    # Pas 3: Procesare (simulată)
    # În producție reală, aici ai apelul către payment gateway (ex: Stripe, PayU)
    print(f"Procesare plată: {suma} EUR prin {metoda}...")

    return {
        "status": "success",
        "mesaj": "Plată procesată cu succes",
        "transaction_id": "TXN-2024-001"  # ID generat de gateway
    }


# ── ENTRY POINT ───────────────────────────────────────────────────────────────

def main():
    """
    Demonstrează funcționalitatea modulului de plăți.

    Returns:
        None: Funcția nu returnează nimic.
    """
    print("=" * 50)
    print("  Payment Processor — Demo")
    print("=" * 50)

    # Test 1: Plată validă
    rezultat = proceseaza_plata(99.99, "card")
    print(f"Test 1: {rezultat['status']} — {rezultat['mesaj']}")

    # Test 2: Sumă invalidă
    rezultat = proceseaza_plata(-10, "card")
    print(f"Test 2: {rezultat['status']} — {rezultat['mesaj']}")

    # Test 3: Metodă invalidă
    rezultat = proceseaza_plata(50.00, "crypto")
    print(f"Test 3: {rezultat['status']} — {rezultat['mesaj']}")

    print("=" * 50)


if __name__ == "__main__":
    main()
