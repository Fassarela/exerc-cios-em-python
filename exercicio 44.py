num = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1
contador = num

print(f"Calculando {num}! = ", end="")

while contador > 0:
    print(f"{contador}", end=" x " if contador > 1 else " = ")
    fatorial *= contador
    contador -= 1

print(f"{fatorial}")
