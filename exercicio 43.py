while True:
    n1 = int(input("Digite o primeiro valor: "))
    n2 =  int(input("Digite o segundo valor: "))
    while True:
        print("\nO que deseja fazer?")
        print("[1]Somar")
        print("[2]Multiplicar")
        print("[3]Mostrar o maior")
        print("[4]Digitar novos números")
        print("[5] Sair do programa")

        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            print(f"A soma entre {n1} e {n2} é {n1 + n2}")
        elif opcao == 2:
            print(f"A multiplicação entre {n1} e {n2} é {n1 * n2}")
        elif opcao == 3:
            maior = max(n1, n2)
            print(f"O maior valor entre {n1} e {n2} é {maior}")
        elif opcao == 4:
            print(f"Vamos digitar novos números!")
            break
        elif opcao == 5:
            print("Finalizando o programa... até breve!")
            exit()
        else:
            print("Opção inválida! Tente novamente")