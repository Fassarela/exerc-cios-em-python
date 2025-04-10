print("=== CALCULADORA DE PREÇO FINAL ===")
preco = float(input("Digite o preço do produto: R$ "))

print("\nFormas de pagamento:")
print("1 - À vista (dinheiro ou cheque) [10% de desconto]")
print("2 - À vista no cartão [5% de desconto]")
print("3 - Em até 2x no cartão [preço normal]")
print("4 - 3x ou mais no cartão [20% de juros]")

opcao = int(input("Escolha a opção (1 a 4): "))

if opcao == 1:
    total = preco * 0.90
elif opcao == 2:
    total = preco * 0.95
elif opcao == 3:
    total = preco
elif opcao == 4:
    total = preco * 1.20
else:
    print("Opção inválida.")
    total = None

if total is not None:
    print(f"\nValor final a pagar: R$ {total:.2f}")
