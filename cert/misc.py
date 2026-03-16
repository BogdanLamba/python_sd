# Funcție care returnează mai multe valori (via tuple)
def min_max(lista):
    return min(lista), max(lista)   # returnează tuple!

numere = [5, 3, 8, 1, 9, 2]
minim, maxim = min_max(numere)      # unpacking direct
print(f"Min: {minim}, Max: {maxim}")