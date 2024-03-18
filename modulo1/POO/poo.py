from operacoes import soma, subtracao, divisao, multiplicacao
# import operacoes
primeiro_numero = int(input("entre com primeiro numero: "))
segundo_numero = int(input("entre com segundo numero numero: "))

resultado_da_soma = soma(primeiro_numero, segundo_numero)
# operacoes.soma(primeiro_numero, segundo_numero)
resultado_da_subtracao = subtracao(primeiro_numero, segundo_numero)
resultado_da_divisao = divisao(primeiro_numero, segundo_numero)
resultado_da_multiplicacao = multiplicacao(primeiro_numero, segundo_numero)

print(resultado_da_soma)
print(resultado_da_subtracao)
print(resultado_da_divisao)
print(resultado_da_multiplicacao)
