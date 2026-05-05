#Editor com a opção de “desfazer”
pilha = []

while True:
    print("\nEDITOR DE TEXTO")
    print("[1] - Digitar palavra")
    print("[2] - Desfazer última palavra")
    print("[3] - Mostrar texto")
    print("[4] - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        palavra = input("Digite uma palavra: ")
        pilha.append(palavra)
        print(f"Palavra adicionada: {palavra}")

    elif opcao == "2":
        if len(pilha) == 0:
            print("Nenhuma palavra para desfazer.")
        else:
            removida = pilha.pop()
            print(f"Palavra removida: {removida}")

    elif opcao == "3":
        if len(pilha) == 0:
            print("Texto atual: (vazio)")
        else:
            print(f"Texto atual: {' '.join(pilha)}")

    elif opcao == "4":
        break

    else:
        print("Opção inválida. Tente novamente.")