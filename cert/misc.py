"""
PCEP-30-02 | Lecția 4.1 — Funcții (Functions)
Fișier: cert/misc.py
Style: Google Docstrings
"""


# ============================================================
# EXERCIȚIUL 1 — Definire și apelare de bază
# ============================================================
# TODO: Definește o funcție greet() care:
#   - primește un parametru name (str)
#   - returnează string-ul "Hello, {name}!"
#   - are un docstring Google Style

# scrie funcția aici
def greet(name: str) -> str:
    """
    Args:
        name (str): numele catre care se face salutarea
    Returns:
        str: un string de tip salutare catre numele introdus
    """
    return f"Hello, {name}!"


# Teste
assert greet("Python") == "Hello, Python!"
assert greet("PCEP") == "Hello, PCEP!"
print("Exercițiul 1: toate testele au trecut ✓")


# ============================================================
# EXERCIȚIUL 2 — Valori returnate multiple
# ============================================================
# TODO: Definește o funcție min_max(numbers) care:
#   - primește o listă de numere
#   - returnează un tuple (minim, maxim)
#   - NU folosește funcțiile built-in min() și max()
#   - are un docstring Google Style
def min_max(numbers: list) -> tuple:
    """
    Finds the minimum and maximum values in a list of numbers.

    Args:
        numbers: a list of numbers.

    Returns:
        A tuple of minium and maxim in the list
    """
    minimum = numbers[0]
    maximum = numbers[0]

    for number in numbers[1:]:
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number

    return minimum, maximum


# scrie funcția aici

# Teste
assert min_max([3, 1, 4, 1, 5, 9]) == (1, 9)
assert min_max([42]) == (42, 42)
assert min_max([-5, 0, 5]) == (-5, 5)
print("Exercițiul 2: toate testele au trecut ✓")


# ============================================================
# EXERCIȚIUL 3 — Parametri cu valori default
# ============================================================
# TODO: Definește o funcție power(base, exponent=2) care:
#   - calculează base ** exponent
#   - are exponent cu valoare default 2 (pătrat)
#   - returnează rezultatul

# scrie funcția aici
def power(base: int, exponent: int =2) -> float:
    return base**exponent


# Teste
assert power(3) == 9        # 3 ** 2
assert power(3, 3) == 27    # 3 ** 3
assert power(2, 0) == 1     # 2 ** 0
print("Exercițiul 3: toate testele au trecut ✓")


# ============================================================
# EXERCIȚIUL 4 — Funcții ca argumente (first-class functions)
# ============================================================
# TODO: Definește o funcție apply(func, values) care:
#   - primește o funcție și o listă de valori
#   - aplică func pe fiecare element și returnează lista rezultatelor
#   - este echivalentul manual al lui map()

# scrie funcția aici
def apply(func, values: list) -> list:
    """
    Applies a function to each element in a list and returns the results.

    Args:
        func: A function to apply to each element.
        values: A list of values.

    Returns:
        A list of results after applying func to each element.
    """
    results = []
    for value in values:
        results.append(func(value))
    return results

# Teste
assert apply(str.upper, ["hello", "world"]) == ["HELLO", "WORLD"]
assert apply(lambda x: x * 2, [1, 2, 3]) == [2, 4, 6]
print("Exercițiul 4: toate testele au trecut ✓")


# ============================================================
# EXERCIȚIUL 5 — Funcție production-like
# ============================================================
def calculate_discount(price: float, discount_pct: float, min_price: float = 0.0) -> float:
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
        raise ValueError(f"price must be >= 0, got {price}")
    if not 0 <= discount_pct <= 100:
        raise ValueError(f"discount_pct must be in [0, 100], got {discount_pct}")

    discounted_price = price * (1 - discount_pct / 100)

    return max(discounted_price, min_price)
    pass

# Teste
assert calculate_discount(100.0, 20.0) == 80.0
assert calculate_discount(100.0, 20.0, min_price=90.0) == 90.0
assert calculate_discount(50.0, 0.0) == 50.0
assert calculate_discount(200.0, 100.0) == 0.0
try:
    calculate_discount(-10.0, 20.0)
    assert False, "Trebuia sa arunce ValueError"
except ValueError:
    pass
print("Exercițiul 5: toate testele au trecut ✓")
