#1) Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

primeiroLado=float(input('Insira o valor do 1º lado: \nResposta:'))
segundoLado=float(input('Insira o valor do 2º lado: \nResposta:'))
tercerceiroLado=float(input('Insira o valor do 3º lado: \nResposta:'))
if primeiroLado<segundoLado+tercerceiroLado and segundoLado<primeiroLado+tercerceiroLado and tercerceiroLado<primeiroLado+segundoLado:
    if primeiroLado==segundoLado==tercerceiroLado:
        tipoTriangulo='equilátero'
    elif primeiroLado==segundoLado or primeiroLado==tercerceiroLado or segundoLado==tercerceiroLado:
        tipoTriangulo='isósceles'
    else:
        tipoTriangulo='escaleno'
    print(f'Essas medidas formam um triângulo {tipoTriangulo}')
else:
    print('Essas medidas não formam um triângulo')
