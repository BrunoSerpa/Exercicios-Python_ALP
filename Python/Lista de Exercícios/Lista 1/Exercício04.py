#04) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
salario = float(input("Digite um salário: R$"))
porcentagem = float(input("Digite quanto o salário irá aumentar: (sem o %)"))
novoSalario = salario*(1+porcentagem/100)
print("O novo salário será: R${}".format(novoSalario))