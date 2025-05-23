num = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado, não foi adicionado')
    r = str(input('Quer continuar?[S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
print(f'Você digiou os valores: {num}')