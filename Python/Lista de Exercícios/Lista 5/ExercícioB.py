"""
    Quantas vezes o trecho de pseudocódigo seguinte imprime 'oi'? 
    para i = 1 até 9
        se i != 3, então
            para j = 1 até 6
                imprime 'oi'
"""
quantPrint=0
for i in range (1, 10):
    if i != 3:
        for j in range (1, 7):
            print('oi')
            quantPrint += 1
print(f'"oi" foi imprimido {quantPrint} vezes')