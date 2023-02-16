#4) Faça um Programa que leia três números e mostre o maior deles.
primeiroNumero=float(input('Insira o 1º número \nResposta:'))
segundoNumero=float(input('Insira o 2º número \nResposta:'))
terceiroNumero=float(input('Insira o 3º número \nResposta:'))
if primeiroNumero>segundoNumero:
    if primeiroNumero>terceiroNumero:
        print(f'o maior número inserido foi {primeiroNumero}')
    else:
        print(f'o maior número inserido foi {terceiroNumero}')
elif segundoNumero>terceiroNumero:
    print(f'o maior número inserido foi {segundoNumero}')
else:
    print(f'o maior número inserido foi {terceiroNumero}')