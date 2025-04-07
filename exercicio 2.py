import math

catetooposto = float(input("Digite o valor do cateto oposto: "))
catetoadjacente = float(input("Digite o valor do cateto adjacente: "))
hipotenusa = math.sqrt(catetooposto**2 + catetoadjacente**2)
print(f"A hipotenusa do triangulo e: {hipotenusa:.2f}")
