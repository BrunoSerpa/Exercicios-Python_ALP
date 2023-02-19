#3) Verifique se um inteiro positivo n é primo.
numeroInteiro = int(input("Digite um número inteiro \nResposta:"))
EncontrouDivisivel, numeroMultiplio = 0, 0
if numeroInteiro <= 1:
    print('{} não é um número primo'.format(numeroInteiro))
else:
    while numeroMultiplio <= numeroInteiro or EncontrouDivisivel < 2:
        numeroMultiplio = numeroMultiplio + 1
        Encontrou = numeroInteiro % numeroMultiplio
        if Encontrou == 0:
            EncontrouDivisivel = EncontrouDivisivel + 1
    if EncontrouDivisivel <= 2:
        print(f"{numeroInteiro} é um número primo")
    else:
        print(f"{numeroInteiro} não é um primo")