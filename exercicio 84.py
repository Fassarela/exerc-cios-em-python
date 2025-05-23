tem = []
principal = []
mai = men = 0
while True:
    tem.append(str(input('Nome: ')))
    tem.append(float(input('Peso: ')))
    if len(principal) == 0:
        mai = men = tem[1]
    else:
        if tem[1] > mai:
            mai = tem[1]
        if tem[1] < men:
            men = tem[1]
    principal.append(tem[:])
    tem.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Os dados foram {principal}')
print(f'Ao todo você cadastrou {len(principal)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de: ', end='')
for p in principal:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi de {men}Kg. Peso de: ', end='')
for p in principal:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')