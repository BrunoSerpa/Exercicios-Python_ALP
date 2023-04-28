#1) Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funções max e min.
import random
numerosSorteados=[]
maiorNumero, menorNumero= 1, 100
for numeroAleatorio in range(10):
    numeroAleatorio = random.randint(1,100)
    if numeroAleatorio>maiorNumero:
        maiorNumero=numeroAleatorio
    if numeroAleatorio<menorNumero:
        menorNumero=numeroAleatorio
    numerosSorteados.append(numeroAleatorio)
print(f'''Dos números sorteados: {numerosSorteados}, o menor número sorteado foi {menorNumero} e o maior foi {maiorNumero}''')