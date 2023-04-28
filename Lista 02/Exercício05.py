#5) Faça um Programa que leia três números e mostre o maior e o menor deles.
primeiroNumero=float(input('Insira o 1º número \nResposta:'))
segundoNumero=float(input('Insira o 2º número \nResposta:'))
terceiroNumero=float(input('Insira o 3º número \nResposta:'))
if primeiroNumero>segundoNumero:
    if primeiroNumero>terceiroNumero:
        if segundoNumero>terceiroNumero:
            print(f'O maior número inserido é {primeiroNumero} e o menor é {terceiroNumero}')
        else:
            print(f'O maior número inserido é {primeiroNumero} e o menor é {segundoNumero}')
    else:
        print(f'O maior número inserido é {terceiroNumero} e o menor é {segundoNumero}')
elif segundoNumero>terceiroNumero:
    if primeiroNumero>terceiroNumero:
            print(f'O maior número inserido é {segundoNumero} e o menor é {terceiroNumero}')
    else:
        print(f'O maior número inserido é {segundoNumero} e o menor é {primeiroNumero}')
else:
    print(f'O maior número inserido é {terceiroNumero} e o menor é {primeiroNumero}')