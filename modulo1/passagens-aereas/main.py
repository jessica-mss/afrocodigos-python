def mostra_menu():
    print("==" * 10)
    print("Escolha uma das opções abaixo: \n"
    "Digite 1 - comprar passagens \n"
    "Digite 2 - listar passagens \n"
    "Digite 3 - sair do sistema \n")
    print("==" * 10)
    print()



while True:
    mostra_menu()
    entrada_do_usuario = int(input())

    if entrada_do_usuario == 1:
        print("Você escolheu comprar passagens")
    elif entrada_do_usuario == 2:
        print("Você escolheu listar passagens")
    elif entrada_do_usuario == 3:
        print("encerrando o programa. Volte Sempre!")
        break
    else:
        print("entrada inválida")
        
   
