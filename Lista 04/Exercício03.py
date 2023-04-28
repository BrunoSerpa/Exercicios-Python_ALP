#3) Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados os dois outros vetores. Imprima os três vetores.
import random
primeiroVetor, segundoVetor, terceiroVetor = [], [], []
elementoAleatorio, quantidadeElementos = 0, 0
while quantidadeElementos <=20:
    quantidadeElementos += 1
    elementoAleatorio = random.randint(1, 100)
    if quantidadeElementos%2!=0:
        primeiroVetor.append(elementoAleatorio)
    else:
        segundoVetor.append(elementoAleatorio)
    terceiroVetor.append(elementoAleatorio)
print(f'1ºVetor:{primeiroVetor}\n2ºVetor:{segundoVetor}\n3ºVetor:{terceiroVetor}')