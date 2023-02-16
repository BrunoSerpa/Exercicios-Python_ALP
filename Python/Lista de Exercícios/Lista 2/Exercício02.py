#2) Determine se um ano é bissexto.
ano=int(input('Digite um ano \nResposta:'))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print('Esse ano é bissexto!')
else:
    print('esse ano não é bissexto!')
