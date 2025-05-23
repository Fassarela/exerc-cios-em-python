lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Caneta', 3,
         'Liqui-paper', 6.90,
         'Apontador', 4,
         'Tesoura', 10,
         'Mochila', 60,
         'Post-it', 7,
         )
print('-'*40)
print(f'{"Listagem de preços: ":^40}')
print('-'*40)
for item in range(0, len(lista)):
    if item % 2 == 0:
        print(f'{lista[item]:.<30}', end='')
    else:
        print(f'R${lista[item]:>7.2f}')
print('-'*40)