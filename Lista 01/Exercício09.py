#09) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
kmRodados=float(input('Insira a quantidade de quilometros percorridos\nresposta:'))
diasAlugados=int(input('Insira a quantidade de dias alugados\nresposta:'))
Aluguel = kmRodados * 0.15 + diasAlugados * 60
print('Deverá se pagar R${:.2f} no aluguel do carro'.format(Aluguel))