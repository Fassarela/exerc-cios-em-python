cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
        'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente.\n')

    print(f'Você digitou o número {cont[num]}')

    continuar = input('Quer continuar? [S/N]: ').strip().upper()
    if continuar != 'S':
        print('Programa encerrado. Até logo!')
        break
