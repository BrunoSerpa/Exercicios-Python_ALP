#05) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
valorMercadoria = float(input("Digite o valor da mercadoria: R$"))
porcentagem = float(input("Digite quanto irá diminuir: (sem o %)"))
desconto= valorMercadoria*porcentagem/100
novoSalario = valorMercadoria-desconto
print(f"O novo valor da mercadoria será: R${novoSalario:.2f} com desconto de: R${desconto:.2f}")
