def é_palindromo(frase):

    frase = frase.replace(" ", "").lower()

    return frase == frase[::-1]


frase = input("Digite uma frase: ")

if é_palindromo(frase):
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")
