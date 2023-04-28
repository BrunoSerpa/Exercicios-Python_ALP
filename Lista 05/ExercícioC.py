#Entre 1067 e 3627 (inclusive), quantos números são pares e também divisíveis por 7?
quantNum = 0
for numero in range(1067, 3628):
    if numero % 2 == 0 and numero % 7 == 0:
        quantNum += 1
print (f'Existem {quantNum} números pares divisíveis por 7 de 1067 a 3627')