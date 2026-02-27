punctaj = 0.85
PRAG_PROMOVARE = 0.70

if punctaj >= PRAG_PROMOVARE:
    print("Promovat")
else:
    print("Picat")

print(f"Punctaj in forma procentuala {punctaj:.1%}")

numar = int(punctaj * 100)
print(f"Decimal:     {numar}")
print(f"Binar:       {numar:b}")
print(f"Octal:       {numar:o}")
print(f"Hexadecimal: {numar:x}")
