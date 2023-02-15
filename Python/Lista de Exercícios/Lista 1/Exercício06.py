#06) Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
velocidade=float(input('insira a velocidade constante que o veículo terá (em km/h) \nresposta:'))
distancia=float(input('insira a distância que o veículo percorrerá (em km) \nresposta:'))
tempo=distancia/velocidade*60
print(f'A viagem terá aproximadamente {tempo:.0f} minutos')
