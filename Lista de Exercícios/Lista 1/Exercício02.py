#02) Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.
valorMetros=float(input('Insira um valor em metros \nresposta: '))
valorMilimetros=valorMetros*10**3
print('{}m é igual {}mm'.format(valorMetros, valorMilimetros))