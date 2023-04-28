#3) Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de  1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
paisA, taxaCrescimentoA = 8*10**4, 0.03
paisB, taxaCrescimentoB = 2*10**5, 0.015
anosNecessario = 0
while paisA<paisB:
    paisA=paisA*(1+taxaCrescimentoA)
    paisB=paisB*(1+taxaCrescimentoB)
    anosNecessario+=1
print(f'Serão necessários {anosNecessario} anos para que a população do país A ultrapasse a população do país B')
print(paisA,'\n', paisB)
