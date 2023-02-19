#1) Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não - negativo n, verificar se n é triangular.
Triangular=False
numeroInteiro=int(input('Digite um número \nResposta:'))
numeroDividindo, Achei = 0, 0
while numeroInteiro != 0 and numeroInteiro != numeroDividindo:
    numeroDividindo = numeroDividindo + 1
    Achei = numeroInteiro % numeroDividindo
    if Achei == 0:
        NumeroTriangular=numeroDividindo*(numeroDividindo+1)*(numeroDividindo+2)
        if numeroInteiro==NumeroTriangular:
            print(f'Esse número é produto de 3 números naturais consecutivos {numeroDividindo}, {numeroDividindo+1} e {numeroDividindo+2}')
            Triangular=True
            break
if Triangular==False:
    print('Esse número não é produto de 3 números naturais consecutivos')

    
