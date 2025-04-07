import random

alunos = []
for i in range(4):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    alunos.append(nome)

random.shuffle(alunos)

print("\nA ordem sorteada para a apresentação do trabalho é:")
for i, aluno in enumerate(alunos, 1):
    print(f"{i} - {aluno}")
