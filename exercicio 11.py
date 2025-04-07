frase = input("Digite um frase: ")
frase_minuscula = frase.upper()
quantidade_a = frase_minuscula.count("A")
primeira_ocorrencia = frase_minuscula.find("A")
ultima_ocorrencia = frase_minuscula.rfind("A")

print(f"A letra 'A' aparece {quantidade_a} vez(es).")
if quantidade_a > 0:
    print(f"A primeira ocorrencia de 'A' esta a posição {primeira_ocorrencia}.")
    print(f"A ultima ocorrencia de 'A' esta a posição {ultima_ocorrencia}.")