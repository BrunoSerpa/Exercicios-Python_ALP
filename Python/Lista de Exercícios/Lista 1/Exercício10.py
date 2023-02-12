#10) Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.
CigarrosDias=int(input('Insira quantos cigarros você fuma por dia \nresposta:'))
TempoFumante=float(input('Insira quantos anos você fuma \nresposta:'))
TempoVidaPerdido=CigarrosDias*(TempoFumante*365)
print('Você perdeu {:.0f} dias de sua vida'.format(TempoVidaPerdido))