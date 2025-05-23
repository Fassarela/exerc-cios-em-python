palavra = ('jesus','Deixa','paz','tenta','fora','nem',
           'socorro','eles','botaram','eu','falei')
for p in palavra:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')