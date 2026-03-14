numere = []
for i in range(5):
    numere.append(int(input(f"Numărul {i + 1}: ")))

print(f"Suma numerelor din lista este {sum(numere)}")
print(f"Media numerelor din lista este {sum(numere) / len(numere):.2f}")
print(f"Minim din lista este {min(numere)}")
print(f"Maximum din lista este {max(numere)}")

print(f"Lista sortata crescator este {sorted(numere)}")
print(f"Lista sortata descrescator este {sorted(numere, reverse=True)}")

media = sum(numere) / len(numere)
for i in range(len(numere) - 1, -1, -1):
    if numere[i] < media:
        del numere[i]
print(f"Lista dupa stergerea elementelor sub medie: {numere}")
