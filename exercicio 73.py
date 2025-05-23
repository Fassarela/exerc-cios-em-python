times = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Bragantino', 'Ceará', 'Bahia',
         'Fluminense', 'Corinthias', 'Atlético Mineiro', 'Botafogo', 'São Paulo',
         'Mirassol', 'Vasco', 'Fortaleza', 'Internacional', 'Vitória', 'Grêmio',
         'Juventude', 'Santos', 'Sport')
print(f'Lista de times: ')
for t in times:
    print(f'-={t}')
print('-=' * 15)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=' * 15)
print(f'Os quatro ultimos são: {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabetica: ')
for t in sorted(times):
    print(f'-={t}')
print('-=' * 15)
print(f'MENGOOOOOOOO está em {times.index("Flamengo")+1}')