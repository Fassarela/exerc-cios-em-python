import math
angulo = float(input("Digite o valor do angulo: "))

angulo_radianos = math.radians(angulo)

seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print(f"O seno de {angulo}° é: {seno:.2f}")
print(f"O cosseno de {angulo}° é: {cosseno:.2f}")
print(f"A tangente de {angulo}° é: {tangente:.2f}")