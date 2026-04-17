"""Modul de validare și formatare a datelor de intrare utilizator."""


def sanitize_input(raw: str, max_length: int = 50) -> str:
    """Curăță și validează un input de tip str de la utilizator.

    Args:
        raw: Textul brut primit de la utilizator.
        max_length: Lungimea maximă permisă după curățare.

    Returns:
        Textul curățat: fără whitespace la capete, lowercase.

    Raises:
        ValueError: Dacă textul rezultat este gol sau depășește max_length.

    Example:
        >>> sanitize_input("  Hello World  ")
        'hello world'
    """
    cleaned = raw.strip().lower()
    if not cleaned:
        raise ValueError("Input-ul nu poate fi gol.")
    if len(cleaned) > max_length:
        raise ValueError(
            f"Input-ul depășește {max_length} caractere (primit: {len(cleaned)})."
        )
    return cleaned


def format_report_line(label: str, value: float, unit: str = "") -> str:
    """Formatează o linie de raport cu aliniere fixă.

    Args:
        label: Eticheta câmpului.
        value: Valoarea numerică.
        unit: Unitatea de măsură (opțional).

    Returns:
        Linie formatată, ex: 'Venit total     :  12345.67 RON'

    Example:
        >>> format_report_line("Venit total", 12345.67, "RON")
        'Venit total     :  12345.67 RON'
    """
    return f"{label:<16}: {value:>10.2f} {unit}".rstrip()


if __name__ == "__main__":
    print(sanitize_input("  Admin User  "))

    lines = [
        format_report_line("Venit total", 125_430.50, "RON"),
        format_report_line("Cheltuieli", 89_210.00, "RON"),
        format_report_line("Profit net", 36_220.50, "RON"),
    ]
    print("\n".join(lines))

# ```
#
# **Output:**
# ```
# admin user
# Venit total     :  125430.50 RON
# Cheltuieli      :   89210.00 RON
# Profit net      :   36220.50 RON