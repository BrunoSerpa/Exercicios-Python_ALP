""" Condicionais if/else/elif
O comando if executa um bloco de comandos somente se a condição é True. Esta condição pode ser qualquer coisa. Os comandos else e elif são opcionais que são testadas apenas quando condições anteriores não forem satisfeitas. 
Programa:

a = ?
if a > 10 and a % 6 == 3:
 print ('A', end = ' ')
elif a > 10 and a < 20:
 print ('B', end = ' ')
else:
 print ('C', end = ' ')

"""
def condicionais(a):
  """ if a==-1:
    print('Feliz Natal!')
    return """
  if a > 10 and a % 6 == 3:
    print ('A', end = ' ')
    """ if a < 20:
      print ('B', end = ' ') """
  elif a > 10 and a < 20:
    print ('B', end = ' ')
  else:
    print ('C', end = ' ')
  print('')
  return
  
  
# Dê os valores de a que produzem a saída ('N/A' se não houver valor possível para a):

def main():
  condicionais(15) #N/A
  condicionais(21) #Qualquer valor multípliplicado por 6 retirando 3 e que seja maior que 10
  condicionais(14) #Qualquer valor de 11 à 19, exceto o 15
  condicionais(1)  #Qualquer valor menor que dez ou maior que 20, que não dão resto 3 se dividos por 6
  condicionais(-1) #N/A

if __name__ == '__main__':
  main()