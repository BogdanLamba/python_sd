def verifica_varsta(varsta):
    """
    Verifica varsta unei persoane si stabileste daca este majora sau minora.

    Args:
        varsta (int): Varsta persoanei in ani.

    Returns:
        str: "Major" daca varsta >= 18, "Minor" altfel.
    """
    if varsta >= 18:
        return "Major"
    else:
        return "Minor"


def proceseaza_cerere():
    # TODO: de implementat logica de procesare a cererii
    pass


if __name__ == "__main__":
    print(f"Varsta 18: {verifica_varsta(18)}")
    print(f"Varsta 1: {verifica_varsta(1)}")
    print(f"Varsta 25: {verifica_varsta(25)}")