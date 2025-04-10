nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media < 5:
    print(f"Média: {media:.1f} - Reprovado")
elif 5 <= media < 7:
    print(f"Média: {media:.1f} - Recuperação")
else:
    print(f"Média: {media:.1f} - Aprovado")
