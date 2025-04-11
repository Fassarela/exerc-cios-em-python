nomes = []
idades = []
sexos = []

soma_idades = 0
homem_mais_velho = None
idade_homem_mais_velho = -1
mulheres_menos_20 = 0

for i in range(4):
    print(f"Pessoa {i+1}:")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").strip().upper()

    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)

    soma_idades += idade

    if sexo == 'M' and idade > idade_homem_mais_velho:
        homem_mais_velho = nome
        idade_homem_mais_velho = idade

    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

media_idade = soma_idades / 4

print("\nResultado:")
print(f"Média de idade do grupo: {media_idade:.2f}")
print(f"Homem mais velho: {homem_mais_velho} com {idade_homem_mais_velho} anos")
print(f"Número de mulheres com menos de 20 anos: {mulheres_menos_20}")
