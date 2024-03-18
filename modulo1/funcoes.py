entrada_do_usuario = int(input("Entre com um numero: "))

def fizzbuzz(meu_numero):
    for num in range(1, meu_numero + 1):
        if num % 15 == 0:
            print("FIZZBUZZ")
        elif num % 5 == 0:
            print("BUZZ")
        if num % 3 == 0:
            print("FIZZ")
        else:
            print(num)
            
fizzbuzz(entrada_do_usuario)