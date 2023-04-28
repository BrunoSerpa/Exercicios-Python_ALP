#03) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
dias = int(input("insira um número de dias\n resposta:"))
horas = int(input("insira um número de horas\n resposta:"))
minutos = int(input("insira um número de minutos\n resposta:"))
segundos = int(input("insira um número de segundos\n resposta:"))
segundosTotais = ((dias * 24 + horas) * 60 + minutos) * 60 + segundos
print(f'Isso tudo é igual a {segundosTotais} segundos')
