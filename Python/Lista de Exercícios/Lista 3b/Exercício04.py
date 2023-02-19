#4) Dado um número inteiro positivo, determine a sua decomposição em fatores primos calculando também a multiplicidade de cada fator.
numeroInteiro = int(input("Digite um número inteiro \nResposta:"))
EncontrouDivisivel, numeroMultiplio, primo = 0, 0, 0
respostaFatorada= str(numeroInteiro) + " fatorado é igual a: "
respostaFatoradaAntiga=respostaFatorada
while True:
    if numeroMultiplio==numeroInteiro or numeroInteiro==1:
        if numeroInteiro==1:
            break
        elif numeroMultiplio<=1:
            respostaFatorada='esse número não é primo'
            break
        elif respostaFatoradaAntiga==respostaFatorada:
            respostaFatorada='esse número é primo'
            break
        else:
            respostaFatorada+='x'+str(numeroMultiplio)
            break
    elif numeroMultiplio>1 and numeroInteiro%numeroMultiplio==0:
        while numeroInteiro%numeroMultiplio==0:
            numeroInteiro/=numeroMultiplio
            primo+=1
        if respostaFatoradaAntiga!=respostaFatorada:
            respostaFatorada+='x'+str(numeroMultiplio)
            if primo!=1:
                respostaFatorada+='^'+str(primo)
        else:
            respostaFatorada+=str(numeroMultiplio)
            if primo!=1:
                respostaFatorada+='^'+str(primo)
    else:
        numeroMultiplio+=1
print(respostaFatorada)