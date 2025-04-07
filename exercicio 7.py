from traceback import print_tb

nome_completo = input("Digite o nome completo: ")
print(f"Nome em maiscula: {nome_completo.upper()}")
print(f"Nome em miusculas: {nome_completo.lower()}")

quantidade_letras = len(nome_completo.replace(" ", ""))
print(f"Quantidade total de letras sem espaços: {quantidade_letras}")

primeiro_nome = nome_completo.split()[0]
quantidade_primeiro_nome = len(primeiro_nome)
print(f"Quantidade de letras o primeiro nome: {quantidade_primeiro_nome}")