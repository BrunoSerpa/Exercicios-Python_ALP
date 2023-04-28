# J. zeros finais
# Verifique quantos zeros há no final de um número inteiro positivo
# Exemplo: 10010 tem 1 zero no fim e 908007000 possui três
def zf(n):
  for quant in range (1, len(str(n))):
    if str(n)[-quant]!="0":
      return quant-1

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))

def main():
  test(zf(10100100010000), 4)
  test(zf(90000000000000000010), 1)

if __name__ == '__main__':
  main()
