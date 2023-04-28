#1) Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
while True:
    nota0a10=input('Insira uma nota de 0 a 10 \nResposta:')
    if not nota0a10.isalpha():
        if 0<=float(nota0a10)<=10:
            print('Valor válido!!')
            break
        else:
            print('Valor inválido, tente novamente!! \n\n')
    else:
        print('Valor inválido, tente novamente!! \n\n')