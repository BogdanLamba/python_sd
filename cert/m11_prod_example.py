"""Modul de procesare a comenzilor dintr-un magazin online."""


def calculate_discount(price: float, discount_pct: float,
                        min_price: float = 0.0) -> float:
    """Calculează prețul final după aplicarea unui discount.

    Args:
        price: Prețul inițial al produsului (>= 0).
        discount_pct: Procentul de discount (0-100).
        min_price: Prețul minim acceptat după discount (default 0.0).

    Returns:
        Prețul final după discount, nu mai mic decât min_price.

    Raises:
        ValueError: Dacă price < 0 sau discount_pct nu este în [0, 100].

    Example:
        >>> calculate_discount(100.0, 20.0)
        80.0
        >>> calculate_discount(100.0, 20.0, min_price=90.0)
        90.0
    """
    if price < 0:
        raise ValueError(f"Prețul nu poate fi negativ: {price}")
    if not (0 <= discount_pct <= 100):
        raise ValueError(f"Discountul trebuie să fie între 0 și 100: {discount_pct}")

    discounted = price * (1 - discount_pct / 100)
    return max(discounted, min_price)


def format_order_summary(items: list, discount_pct: float = 0.0) -> str:
    """Formatează un sumar de comandă cu discount aplicat.

    Args:
        items: Listă de tuple (nume, preț).
        discount_pct: Discount global aplicat pe toată comanda.

    Returns:
        String formatat cu itemii, totalul și discountul aplicat.

    Example:
        >>> format_order_summary([("Laptop", 4999.99)], discount_pct=10.0)
        '...'
    """
    lines = ["=" * 40, f"{'COMANDĂ':^40}", "=" * 40]

    total = 0.0
    for name, price in items:
        final = calculate_discount(price, discount_pct)
        lines.append(f"{name:<25} {final:>10.2f} RON")
        total += final

    lines += ["─" * 40, f"{'TOTAL':<25} {total:>10.2f} RON", "=" * 40]
    return "\n".join(lines)


if __name__ == "__main__":
    order = [
        ("Laptop ProBook", 4999.99),
        ("Mouse Wireless", 149.99),
        ("Tastatura Mec.", 399.99),
    ]
    print(format_order_summary(order, discount_pct=15.0))