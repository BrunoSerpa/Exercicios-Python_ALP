#5) Faça um programa que peça um inteiro positivo e o mostre invertido.
numeroInteiro=input('Digite um Número \nResposta:')
numeroAntigo=numeroInteiro
numeroInvertido=''
while numeroInteiro!='':
    quantidadeDeCaracteres = len(numeroInteiro)
    ultimoCaracter = numeroInteiro[quantidadeDeCaracteres-1:]
    numeroInvertido=numeroInvertido+ultimoCaracter
    numeroInteiro= numeroInteiro[:quantidadeDeCaracteres-1]
print(f'Com seus caractéres invertidos fica {int(numeroInvertido)}')