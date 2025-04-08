reta1 = float(input("Digite o tamanho da primeira reta: "))
reta2 = float(input("Digite o tamanho da segunda reta: "))
reta3 = float(input("Digite o tamanho da terceira reta: "))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print("As retas podem formar um triângulo.")
else:
    print("As retas não podem formar um triângulo.")
