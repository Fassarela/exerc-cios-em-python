import random

opcoes = ["pedra", "papel", "tesoura"]

print("=== JOKENPÔ ===")
print("Escolha uma opção:")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")

jogador = int(input("Digite o número da sua escolha: "))

if jogador < 1 or jogador > 3:
    print("Opção inválida!")
else:
    jogador_escolha = opcoes[jogador - 1]
    computador_escolha = random.choice(opcoes)

    print(f"\nVocê escolheu: {jogador_escolha}")
    print(f"Computador escolheu: {computador_escolha}")

    if jogador_escolha == computador_escolha:
        print("Empate!")
    elif (jogador_escolha == "pedra" and computador_escolha == "tesoura") or \
         (jogador_escolha == "papel" and computador_escolha == "pedra") or \
         (jogador_escolha == "tesoura" and computador_escolha == "papel"):
        print("Você venceu!")
    else:
        print("Computador venceu!")
