ano_de_nascimento = int(input("Informe o ano de nascimento do atleta: "))
idade = 2025 - ano_de_nascimento

if idade <= 9:
    print("Mirim")
elif 9 < idade <= 14:
    print("Infantil")
elif 14 < idade <= 19:
    print("Junior")
elif 19 < idade <= 20:
    print("Sênior")
else:
    print("Master")
