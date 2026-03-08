n = int(input("Introdu un număr întreg: "))

if n == 0:
    print("Zero")
elif n > 0 and n % 2 == 0:
    print("Pozitiv par")
elif n > 0 and n % 2 != 0:
    print("Pozitiv impar")
elif n < 0 and n % 2 == 0:
    print("Negativ par")
else:
    print("Negativ impar")

if n % 3 == 0 and n % 5 == 0:
    print("Divizibil cu 3 și cu 5 (FizzBuzz!)")
elif n % 3 == 0:
    print("Divizibil cu 3 (Fizz)")
elif n % 5 == 0:
    print("Divizibil cu 5 (Buzz)")
else:
    print("Nu este divizibil nici cu 3, nici cu 5")
