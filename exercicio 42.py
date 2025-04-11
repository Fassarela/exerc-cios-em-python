import  random
numero_secreto = random.randint(0, 10)
palpite = -1 #caso o valor fosse 0 e o núm. escolhido fosse 0 , o jogador iria ganhar logo de cara, por isso colocamos em -1
tentativas = 0
print("Tente advinhar o número que estou pensando (entre 0 e 10)!")

while palpite != numero_secreto:
    try:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1
        if palpite < 0 or palpite > 10:
            print("Por favor, digite um número entre 0 e 10:")
        elif palpite < numero_secreto:
            print("Mais... tente um número maior.")
        elif palpite > numero_secreto:
            print("Menor... tente um número menor.")
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")
print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativa(s).")