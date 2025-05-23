lista = []
for num in range(5):
    num = int(input("Digite um número: "))
    c = 0
    while c < len(lista) and num > lista[c]:
        c += 1
    lista.insert(c, num)
    print("Item adicionado", f"na posição {c}" if c < len(lista) - 1 else "no final", "da lista")
print(f"\nLista ordenada: {lista}")