suma = 0
for i in range(1, 101):
    suma += i
print(f"Suma numerelor de la 1 la 100 este {suma}")

i = 1
while i <= 1000:
    if i % 7 == 0 and i % 11 == 0:
        print(f"Primul numar din intervalul [1, 1000] care este divizibil cu 7 și cu 11 simultan este {i}")
        break
    i += 1

number = 97
for i in range(2, number):
    if number % i == 0:
        print(f"Numarul nu este prim, este divizibil cu: {i}!")
        break
else:
    print(f"Numarul {number} este prim!")
