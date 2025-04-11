primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

termo = primeiro
contador = 1
total = 0
mais = 10

print("\nProgressão Aritmética:")

while mais != 0:
    total += mais
    while contador <= total:
        print(f"{termo}", end=" → " if contador < total else " → FIM\n")
        termo += razao
        contador += 1
    mais = int(input("Quantos termos a mais você quer mostrar? (0 para encerrar): "))

print(f"\nProgressão finalizada com {total} termos mostrados.")
