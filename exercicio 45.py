primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

termo = primeiro
contador = 1

print("\nOs 10 primeiros termos da PA são:")

while contador <= 10:
    print(f"{termo}", end=" → " if contador < 10 else " → FIM\n")
    termo += razao
    contador += 1
