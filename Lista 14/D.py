# D. Dada uma lista de números retorna uma lista sem os elementos repetidos
def remove_iguais(nums):
  novalista=[]
  for num in nums:
    if num in novalista: continue
    novalista.append(num)
  return sorted(novalista)

def test(obtido, esperado):
  if obtido == esperado: prefixo = ' Parabéns!'
  else: prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))

test(remove_iguais([2, 2, 1, 3]), [1, 2, 3])
test(remove_iguais([2, 2, 3, 2, 3]), [2, 3])
test(remove_iguais([]), [])