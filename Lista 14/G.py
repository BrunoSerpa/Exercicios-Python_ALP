# G. Soma em listas invertidas
# Colocamos os dígitos de dois números em listas ao contrário (513 vira [3, 1, 5] e 295 vira [5, 9, 2]
# [3, 1, 5] + [5, 9, 2] = [8, 0, 8]
# pode supor que n1 e n2 tem o mesmo número de dígitos
# Não vale converter a lista em número para somar diretamente
def soma(n1, n2):
  n3, sobe = [], 0
  for num in range(0, len(n1)):
    if n1[num] + n2[num] + sobe > 9: n3.append(n1[num] + n2[num] + sobe - 10) 
    else: n3.append(n1[num] + n2[num] + sobe)  
    sobe = 0 if n1[num] + n2[num] + sobe < 10 else 1
  if sobe ==1: n3.append(sobe)
  return n3

def test(obtido, esperado):
  if obtido == esperado: prefixo = ' Parabéns!'
  else: prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))

test(soma([5, 2, 3, 4], [9, 8, 7, 8]), [4, 1, 1, 3, 1])
test(soma([3, 1, 5], [5, 9, 2]), [8, 0, 8])