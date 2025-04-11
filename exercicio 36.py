import math

def é_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Digite um número para verificar se é primo: "))
if é_primo(n):
    print(f"{n} é um número primo.")
else:
    print(f"{n} não é um número primo.")
