sexo = input('Informe seu genêro [M/F]: ').strip().upper()
while sexo not in ['M','F']:
    print("Valor inválido! Por favor, digite apenas 'M' para masculino e 'F' para feminino")
    sexo = input('Informe seu genêro [M/F]: ').strip().upper()
print(f"Sexo '{sexo}' registrado com sucesso")
