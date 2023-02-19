#5) Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides.
primeiroNumero=int(input('Insira um número \nResposta:'))
segundoNumero=int(input('Insira outro número \nResposta:'))

anterior= primeiroNumero
atual= segundoNumero
resto = atual%anterior
while resto != 0:
    resto = anterior % atual;
    anterior = atual;
    atual = resto;
mdc = anterior
print(f'O mdc de {primeiroNumero} e {segundoNumero} é {mdc}')