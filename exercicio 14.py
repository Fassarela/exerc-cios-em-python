velocidade = float(input("Informe a velocidade do carro em km/h: "))

limite_velocidade = 80
if velocidade > limite_velocidade:
    excesso = velocidade - limite_velocidade
    multa = excesso * 7
    print(f"Você não está no filme do Velozes e Furiosos, parabéns você foi multado! O valor da multa é R$ {multa:.2f}.")
else:
    print("A velocidade está dentro do limite. Não há multa.")
