print("Digite um numero: ")

resposta = int(input())

if resposta % 3 == 0:
    print("FIZZ")
elif resposta % 5 == 0:
    print("BUZZ")
elif resposta % 5 == 0 and resposta % 3 == 0:
    print("FIZZBUZZ")
else:
    print(resposta)
    
    
    
if resposta % 5 == 0 and resposta % 3 == 0:
    print("FIZZBUZZ")
elif resposta % 5 == 0:
    print("BUZZ")
elif resposta % 3 == 0:
    print("FIZZ")
else:
    print(resposta)