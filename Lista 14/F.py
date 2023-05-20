# F. Derivada de um polinômio
# Os coeficientes de um polinômio estão numa lista na ordem do seu grau. Você deverá devolver uma lista com os coeficientes da derivada.
# Exemplo: [3, 2, 5, 2] retorna [2, 10, 6]
# A derivada de 3 + 2x + 5x^2 + 2x^3 é 2 + 10x + 6x^2

def derivada(coef):
  novalista=[]
  for n in range(1, len(coef)): novalista.append(coef[n]*n)
  return novalista

def test(obtido, esperado):
  if obtido == esperado: prefixo = ' Parabéns!'
  else: prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))


test(derivada([3, 0, 4, 3, 5]), [0, 8, 9, 20])
test(derivada([4, 16, 1]), [16, 2])