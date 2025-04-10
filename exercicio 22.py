a = float(input('Valor Casa: R$'))
b = int(input('Quantos anos quer pagar? '))
c = float(input('Salário: R$'))

d = a / (b * 12)

e = c * 0.30

if d <= e:
    print(f'Seu empréstimo foi aprovado! Suas parcelas serão de R$ {d:.2f} por mês.')
else:
    print(f'Seu empréstimo foi recusado. O valor da parcela mensal de R$ {d:.2f} ultrapassou 30% de sua renda mensal de R$ {c:.2f}.')
