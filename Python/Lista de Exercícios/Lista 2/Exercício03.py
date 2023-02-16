#3) João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO.
pesoPeixe=float(input('Insira o peso dos peixes \nResposta:'))
if pesoPeixe>50:
    pesoExcedente=pesoPeixe-50
    multa=4*pesoExcedente
    print(f'Peso ultrapassado: {pesoExcedente:.2f} kg, multa a se pagar: R${multa:.2f}.')
else:
    pesoExcedente, multa= 0, 0
    print(f'Peso ultrapassado: {pesoExcedente:.2f} kg, multa a se pagar: R${multa:.2f}.')