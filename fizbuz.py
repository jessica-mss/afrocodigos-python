
max_numero = 15

for numero in range(1, max_numero + 1):
    if numero % 3 == 0 and numero % 5 == 0:
        print("FIZZBUZZ")
    elif numero % 3 == 0:
        print("FIZZ")
    elif numero % 5 == 0:
        print("BUZZ")
    else:
        print(numero)
