distancia = int(input("Digite a distância: "))
if distancia > 200:
    m = distancia * 0.45
    print(f"A distancia foi de {distancia}km e o valor da viagem ficou R${m}")
else:
    m = distancia * 0.5
    print(f"A distancia foi de  {distancia}km e o valor da viagem ficou R${m}")