menor_idade = 0
maior_idade = 0

for i in range(7):
    ano_de_nascimento = int(input('Digite o ano de nascimento: '))
    idade = 2025 - ano_de_nascimento

    if idade < 18:
        menor_idade += 1
        print('Você é de menor')
    else:
        maior_idade += 1
        print('Você é de maior')

print(f'\nNúmero de pessoas menores de idade: {menor_idade}')
print(f'Número de pessoas maiores de idade: {maior_idade}')
