numero = int(input("Digite um número inteiro: "))

print("Escolha a base de conversão:")
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")
base = int(input("Digite o número da base (1, 2 ou 3): "))

if base == 1:

    print(f"O número {numero} em binário é: {bin(numero)[2:]}")
elif base == 2:

    print(f"O número {numero} em octal é: {oct(numero)[2:]}")
elif base == 3:

    print(f"O número {numero} em hexadecimal é: {hex(numero)[2:].upper()}")
else:
    print("Opção inválida. Escolha entre 1, 2 ou 3.")
