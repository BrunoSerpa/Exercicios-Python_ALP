#2) Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os números ímpares na lista IMPAR. Imprima as três listas.
import random
numerosSorteados, numerosPares, numerosImpares=[], [], []
for numeroAleatorio in range(20):
    numeroAleatorio = random.randint(1,100)
    if numeroAleatorio%2==0:
        numerosPares.append(numeroAleatorio)
    else:
        numerosImpares.append(numeroAleatorio)
    numerosSorteados.append(numeroAleatorio)
print(f'''Os números sorteados foram: {numerosSorteados};
Os número pares foram: {numerosPares};
Os números impares foram{numerosImpares}.''')