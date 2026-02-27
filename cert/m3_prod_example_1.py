# config.py — Fișier de configurare tipic într-o aplicație reală

"""
Application Configuration Module (Modul de configurare)

Centralizează toate constantele și setările aplicației.
Modifică valorile DOAR în acest fișier — niciodată hardcodat în cod.
"""

# ── CONSTANTE NUMERICE ────────────────────────────────────────────────────────

# Integer constants (constante întregi)
MAX_LOGIN_ATTEMPTS  = 3            # Blocare cont după 3 încercări eșuate
SESSION_TIMEOUT_SEC = 1_800        # 30 minute în secunde (lizibil cu _)
MAX_FILE_SIZE_BYTES = 10_485_760   # 10 MB în bytes (10 * 1024 * 1024)

# Float constants (constante float)
TAX_RATE        = 0.19     # TVA 19% în România
MIN_PASS_SCORE  = 0.7      # Scor minim pentru promovare — 70%
INTEREST_RATE   = 1.5e-2   # Rata dobânzii — 0.015 (1.5%)

# Boolean flags (fanioane booleene)
DEBUG_MODE      = False    # Dezactivat în producție
MAINTENANCE     = False    # Activat în timpul mentenanței
EMAIL_VERIFY    = True     # Verificarea email-ului obligatorie

# Hexadecimal — folosit frecvent pentru culori, permisiuni, adrese
COLOR_PRIMARY   = 0x1F4E79    # Albastru închis — culoarea brandului
COLOR_SUCCESS   = 0x1E6B3C    # Verde — succes
COLOR_ERROR     = 0x7B1818    # Roșu — eroare
FILE_PERMISSION = 0o755       # Permisiuni Unix: owner=rwx, group=rx, others=rx

# None — valori nesetate implicit
ADMIN_EMAIL     = None     # Setat la prima configurare
API_KEY         = None     # Injectat din environment variables


# ── FUNCȚII CONFIGURARE ────────────────────────────────────────────────────────

def get_config_summary():
    """
    Returnează un rezumat al configurației curente.

    Returns:
        dict: Dicționar cu setările principale ale aplicației.
    """
    return {
        "debug": DEBUG_MODE,
        "maintenance": MAINTENANCE,
        "session_timeout_min": SESSION_TIMEOUT_SEC // 60,   # convertim la minute
        "tax_rate_percent": TAX_RATE * 100,                  # 0.19 → 19.0
        "max_file_mb": MAX_FILE_SIZE_BYTES / 1_048_576,      # bytes → MB
    }


def validate_score(scor):
    """
    Validează dacă un scor este suficient pentru promovare.

    Args:
        scor (float): Scorul obținut, între 0.0 și 1.0.

    Returns:
        bool: True dacă scorul depășește pragul minim.
    """
    # Verificăm că scorul e în intervalul valid [0.0, 1.0]
    if not 0.0 <= scor <= 1.0:
        return False

    return scor >= MIN_PASS_SCORE


if __name__ == "__main__":
    config = get_config_summary()
    print("=== Configurație aplicație ===")
    for cheie, valoare in config.items():
        print(f"  {cheie}: {valoare}")

    print("\n=== Teste validate_score ===")
    teste = [0.95, 0.70, 0.65, 0.0, 1.5]
    for scor in teste:
        rezultat = validate_score(scor)
        print(f"  Scor {scor}: {'Promovat' if rezultat else 'Picat/Invalid'}")
