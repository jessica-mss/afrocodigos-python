# entrada_do_usuario = int(input("Entre com um numero: "))

def fatorial(numero):
    soma = 0
    while numero > 0:
        print("O contador é:", numero)
        soma += numero
        numero -= numero        
    print(soma)
        
fatorial(5)
        
