numero_1 = int(input("Me diga o primero número a ser somado"))
numero_2 = int(input("Me diga o segundo número a ser somado"))

def soma(primeiro_numero, segundo_numero):
    return primeiro_numero+segundo_numero

resultado_da_soma = soma(numero_1, numero_2)
print(f"O resultado da soma é: {resultado_da_soma}")