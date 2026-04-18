"""
PCEP-30-02 | Lecția 4.3 — Ierarhia Excepțiilor
Fișier: cert/misc.py
Style: Google Docstrings
"""


# ============================================================
# EXERCIȚIUL 1 — Identificare excepții
# ============================================================
# TODO: Pentru fiecare bloc de cod de mai jos, scrie ce excepție
# este aruncată și de ce (ca string în variabila corespunzătoare).
# Rulează codul mental sau în consolă, NU în assert-uri.

# a) Ce excepție aruncă acest cod?
# int("abc")
ex1a = ""  # ex: "ValueError"

# b) Ce excepție aruncă acest cod?
# x = [1, 2, 3]; print(x[10])
ex1b = ""

# c) Ce excepție aruncă acest cod?
# result = 10 / 0
ex1c = ""

# d) Ce excepție aruncă acest cod?
# d = {"a": 1}; print(d["z"])
ex1d = ""

# e) Ce excepție aruncă acest cod?
# print(undefined_variable)
ex1e = ""

assert ex1a == "ValueError",   f"1a gresit, ai: {ex1a}"
assert ex1b == "IndexError",   f"1b gresit, ai: {ex1b}"
assert ex1c == "ZeroDivisionError", f"1c gresit, ai: {ex1c}"
assert ex1d == "KeyError",     f"1d gresit, ai: {ex1d}"
assert ex1e == "NameError",    f"1e gresit, ai: {ex1e}"
print("Exercițiul 1: toate testele au trecut ✓")


# ============================================================
# EXERCIȚIUL 2 — Ierarhia: isinstance() cu excepții
# ============================================================
# TODO: Completează valorile de True/False bazate pe ierarhia
# de excepții Python (fără să rulezi codul — gândește ierarhia).

# ValueError este subclasă a Exception?
q2a = None   # True sau False

# ZeroDivisionError este subclasă a ArithmeticError?
q2b = None

# IndexError este subclasă a LookupError?
q2c = None

# Exception este subclasă a BaseException?
q2d = None

# KeyboardInterrupt este subclasă a Exception?
q2e = None   # Atentie — acesta e o capcana!

assert q2a is True,  "2a: ValueError IS-A Exception"
assert q2b is True,  "2b: ZeroDivisionError IS-A ArithmeticError"
assert q2c is True,  "2c: IndexError IS-A LookupError"
assert q2d is True,  "2d: Exception IS-A BaseException"
assert q2e is False, "2e: KeyboardInterrupt NU este subclasa a Exception!"
print("Exercițiul 2: toate testele au trecut ✓")


# ============================================================
# EXERCIȚIUL 3 — try / except de bază
# ============================================================
# TODO: Implementează funcția safe_divide(a, b) care:
#   - împarte a la b
#   - dacă b este 0, returnează None (fără să crape)
#   - dacă a sau b nu sunt numere, returnează None
#   - altfel returnează rezultatul ca float

def safe_divide(a, b):
    """Împarte a la b în mod sigur.

    Args:
        a: Deîmpărțitul.
        b: Împărțitorul.

    Returns:
        Rezultatul ca float, sau None dacă operația eșuează.

    Example:
        >>> safe_divide(10, 2)
        5.0
        >>> safe_divide(10, 0)
        None
    """
    # TODO: implementează cu try/except
    pass


assert safe_divide(10, 2)   == 5.0
assert safe_divide(10, 0)   is None
assert safe_divide("x", 2)  is None
assert safe_divide(9, 3)    == 3.0
print("Exercițiul 3: toate testele au trecut ✓")


# ============================================================
# EXERCIȚIUL 4 — except multiplu + else + finally
# ============================================================
# TODO: Implementează funcția parse_int(value) care:
#   - încearcă să convertească value la int
#   - dacă reușește: afișează "Conversie reușită: {result}" și returnează int-ul
#   - dacă ValueError: afișează "Eroare: nu e număr valid" și returnează None
#   - dacă TypeError: afișează "Eroare: tip invalid" și returnează None
#   - INDIFERENT de rezultat: afișează "Operație finalizată."

def parse_int(value):
    """Convertește o valoare la int cu tratare explicita a erorilor.

    Args:
        value: Valoarea de convertit.

    Returns:
        int dacă conversia reușește, None altfel.
    """
    # TODO: implementează cu try / except ValueError / except TypeError / finally
    pass


assert parse_int("42")   == 42
assert parse_int("abc")  is None
assert parse_int(None)   is None
assert parse_int("7")    == 7
print("Exercițiul 4: toate testele au trecut ✓")


# ============================================================
# EXERCIȚIUL 5 — raise + excepție custom
# ============================================================
class InvalidAgeError(ValueError):
    """Excepție aruncată când vârsta introdusă este invalidă."""
    pass


def validate_age(age: int) -> str:
    """Validează vârsta unui utilizator.

    Args:
        age: Vârsta de validat.

    Returns:
        Categoria de vârstă: 'minor', 'adult', sau 'senior'.

    Raises:
        InvalidAgeError: Dacă age < 0 sau age > 150.
        TypeError: Dacă age nu este int.

    Example:
        >>> validate_age(25)
        'adult'
        >>> validate_age(-1)
        InvalidAgeError: Varsta invalida: -1
    """
    # TODO: implementează funcția
    pass


assert validate_age(10)  == "minor"
assert validate_age(30)  == "adult"
assert validate_age(70)  == "senior"

try:
    validate_age(-1)
    assert False, "Trebuia sa arunce InvalidAgeError"
except InvalidAgeError:
    pass

try:
    validate_age(200)
    assert False, "Trebuia sa arunce InvalidAgeError"
except InvalidAgeError:
    pass

try:
    validate_age("treizeci")
    assert False, "Trebuia sa arunce TypeError"
except TypeError:
    pass

print("Exercițiul 5: toate testele au trecut ✓")

# ============================================================
# EXERCIȚIUL 1 — *args
# ============================================================
# TODO: Definește o funcție summation(*args) care:
#   - acceptă oricâte argumente numerice
#   - returnează suma lor
#   - dacă nu primește niciun argument, returnează 0
# scrie funcția aici
def summation(*args):
    if args is None:
        return 0
    return sum(args)


# Teste
assert summation() == 0
assert summation(1, 2, 3) == 6
assert summation(10, -5, 2) == 7
print("Exercițiul 1: toate testele au trecut ✓")


# ============================================================
# EXERCIȚIUL 2 — **kwargs
# ============================================================
# TODO: Definește o funcție build_profile(**kwargs) care:
#   - acceptă oricâte keyword arguments
#   - returnează un dict cu toate perechile cheie-valoare primite
#   - adaugă automat cheia "active": True la orice profil

# scrie funcția aici
def build_profile(**kwargs):
    kwargs["active"] = True
    return kwargs


# Teste
result = build_profile(name="Ana", role="admin")
assert result == {"name": "Ana", "role": "admin", "active": True}
result2 = build_profile()
assert result2 == {"active": True}
print("Exercițiul 2: toate testele au trecut ✓")

# ============================================================
# EXERCIȚIUL 3 — Scope: local vs global
# ============================================================
# TODO: Completează funcțiile de mai jos respectând regulile de scope.

counter = 0  # variabilă globală


# a) Definește increment() care incrementează counter-ul global cu 1
#    Hint: folosește 'global'

# scrie funcția aici
def increment():
    global counter
    counter += 1

# b) Definește get_counter() care returnează valoarea curentă a counter-ului

# scrie funcția aici
def get_counter():
    global counter
    return counter

# Teste
increment()
increment()
increment()
assert get_counter() == 3
print("Exercițiul 3: toate testele au trecut ✓")


# ============================================================
# EXERCIȚIUL 4 — Combinat: *args + **kwargs
# ============================================================
# TODO: Definește o funcție log_event(event, *tags, **metadata) care:
#   - event (str): numele evenimentului — parametru pozițional obligatoriu
#   - *tags: taguri opționale ca strings
#   - **metadata: perechi cheie-valoare opționale
#   - returnează un dict cu structura:
#     {"event": event, "tags": list(tags), "metadata": metadata}

# scrie funcția aici
def log_event(event, *tags, **metadata):
    """
    Loghează un eveniment cu taguri și metadate opționale.

    Args:
        event (str): numele evenimentului
        *tags: taguri opționale ca strings
        **metadata: perechi cheie-valoare opționale

    Returns:
        dict: {"event": ..., "tags": [...], "metadata": {...}}
    """
    return {
        "event": event,
        "tags": list(tags),
        "metadata": metadata
    }

#Teste
result = log_event("login", "auth", "web", user="ana", ip="127.0.0.1")
assert result["event"] == "login"
assert result["tags"] == ["auth", "web"]
assert result["metadata"] == {"user": "ana", "ip": "127.0.0.1"}
print("Exercițiul 4: toate testele au trecut ✓")


# ============================================================
# EXERCIȚIUL 5 — Funcție production-like
# ============================================================
def format_table(headers: tuple, rows: list, col_width: int = 15) -> str:
    """Formatează date tabulare ca string aliniat.

    Args:
        headers: Tuple cu numele coloanelor.
        rows: Listă de tuple, fiecare reprezentând un rând.
        col_width: Lățimea fiecărei coloane în caractere (default 15).

    Returns:
        String formatat cu header, separator și rânduri aliniate la stânga.

    Example:
        >>> print(format_table(("Nume", "Rol"), [("Ana", "admin")]))
        Nume           Rol
        ---------------...
        Ana            admin
    """
    header_line = "".join(col.ljust(col_width) for col in headers)

    # 2. Separatorul — lățime totală = col_width * număr coloane
    separator = "-" * (col_width * len(headers))

    # 3. Rândurile de date — același pattern ca header-ul
    data_lines = [
        "".join(str(cell).ljust(col_width) for cell in row)
        for row in rows
    ]

    # 4. Asamblare finală
    all_lines = [header_line, separator] + data_lines
    return "\n".join(all_lines)

# Teste
headers = ("Nume", "Rol", "Status")
rows = [
    ("Ana", "admin", "activ"),
    ("Ion", "user", "inactiv"),
]
output = format_table(headers, rows, col_width=12)
assert "Nume" in output
assert "Ana" in output
assert "inactiv" in output
print("Exercițiul 5: toate testele au trecut ✓")
