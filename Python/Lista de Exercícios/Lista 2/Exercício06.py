#6) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto-Descontos = Salário Líquido. Calcule os descontos e o salário líquido, conforme a tabela abaixo:
#a. + Salário Bruto : R$
#b. - IR (11%) : R$
#c. - INSS (8%) : R$
#d. - Sindicato (5%) : R$
#e. = Salário Liquido : R$
GanhosHoras=float(input('Insira quantos você recebe por hora \nResposta:'))
HorasMes=float(input('Insira quantas horas você trabalha por mês \nResposta:'))
salarioBruto=GanhosHoras*HorasMes
impostoDeRenda, inss, sindicato = salarioBruto*0.11, salarioBruto*0.08, salarioBruto*0.05
descontos = impostoDeRenda + inss + sindicato
salarioLiquido = salarioBruto - descontos
print(f'\nSalário Bruto: R${salarioBruto:.2f}\nImposto de Renda (11%): R${impostoDeRenda:.2f}\nINSS (8%): R${inss:.2f}\nSindicato (5%): R${sindicato:.2f}\nSalário Líquido: R${salarioLiquido:.2f}\n')