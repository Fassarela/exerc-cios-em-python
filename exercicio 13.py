import random

numero_computador = random.randint(0, 5)

numero_usuario = int(input("Olá, já pensei em um número inteiro entre 0 e 5 tente advinha-lo!: "))

if numero_usuario == numero_computador:
    print("Parabéns! Você acertou!")
else:
    print(f"Que pena! O número escolhido pelo computador era {numero_computador}. Tente novamente!")
