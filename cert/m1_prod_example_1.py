# main.py — Entry point-ul oricărei aplicații Python profesionale

import sys  # Standard library module (modul din biblioteca standard) pentru info despre sistem


def main():
    """
    Main function (funcția principală) a aplicației.

    În producție, TOATĂ logica aplicației pornește de aici.
    Aceasta este o docstring (documentație) — bună practică în orice cod serios.
    """

    # Verificăm versiunea Python (ce interpreter (interpretor) este instalat)
    python_version = sys.version
    major_version = sys.version_info.major  # ex: 3
    minor_version = sys.version_info.minor  # ex: 11

    print("=" * 40)
    print("  Sistem de gestiune pornit")
    print("=" * 40)
    print(f"Interpreter (Interpretor) Python: {major_version}.{minor_version}")
    print(f"Detalii complete: {python_version}")
    print(f"Platform (Platformă): {sys.platform}")
    print("Status: Aplicație inițializată cu succes.")
    print("=" * 40)

if __name__ == "__main__":
    main()