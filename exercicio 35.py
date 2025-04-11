primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razão = int(input("Digite a razão da PA: "))

print("Os 10 primeiros termos da PA são:")
for i in range(10):
    termo_atual = primeiro_termo + i * razão
    print(termo_atual)
