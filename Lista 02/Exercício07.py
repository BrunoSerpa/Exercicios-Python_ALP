#7) Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.
TamanhoParede=float(input('Insira o tamanho da parede (em m²) \nResposta:'))
LataTinta=TamanhoParede/54
if LataTinta.__float__:
    QuantidadeLataTinta=int(LataTinta+1)
Valor=80*QuantidadeLataTinta
print(f'Será necessário {QuantidadeLataTinta} latas, ou seja, R${Valor:.2f}')