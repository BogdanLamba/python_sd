# guess_game.py — Joc de ghicit numărul

"""
Number Guessing Game Module

Joc simplu în care utilizatorul trebuie să ghicească
un număr ales de program, cu feedback la fiecare încercare.
"""

import random

# ── CONSTANTE ──────────────────────────────────────────────────────────────
MIN_NR       = 1
MAX_NR       = 100
MAX_INCERCARI = 7


def joaca():
    """
    Rulează un joc complet de ghicit numărul.

    Returns:
        None
    """
    numar_secret = random.randint(MIN_NR, MAX_NR)
    incercari    = 0

    print("=" * 40)
    print(f"  Ghicește numărul ({MIN_NR}-{MAX_NR})!")
    print(f"  Ai {MAX_INCERCARI} încercări.")
    print("=" * 40)

    while incercari < MAX_INCERCARI:
        incercari += 1
        ramase = MAX_INCERCARI - incercari

        ghicit = int(input(f"\nÎncercarea {incercari}/{MAX_INCERCARI}: "))

        if ghicit == numar_secret:
            print(f"✅ Corect! Ai ghicit în {incercari} încercări!")
            break
        elif ghicit < numar_secret:
            print(f"📈 Prea mic! Mai ai {ramase} încercări.")
        else:
            print(f"📉 Prea mare! Mai ai {ramase} încercări.")
    else:
        # else se execută DOAR dacă while s-a terminat fără break
        # adică utilizatorul a epuizat toate încercările
        print(f"\n❌ Ai pierdut! Numărul era {numar_secret}.")


if __name__ == "__main__":
    joaca()