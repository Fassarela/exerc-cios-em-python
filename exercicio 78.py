lista = []
for cont in range(0,5):
    lista.append(int(input(f'Digite um valor na posição {cont}: ')))
print(f'O maior foi {max(lista)} na posição {lista.index(max(lista))} e o menor foi: {min(lista)} e na posição {lista.index(min(lista))}')
print('Fim do Programa')
