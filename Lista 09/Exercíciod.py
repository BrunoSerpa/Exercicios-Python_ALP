#!/usr/bin/python -tt
# Exercícios by Nick Parlante (CodingBat)

# D. maior_ponta #
# Dada uma lista não vazia, cria uma nova lista onde todos
# os elementos são o maior das duas pontas
# obs.: não é o maior de todos, mas entre as duas pontas
# maior_ponta([1, 2, 3]) -> [3, 3, 3]
# maior_ponta([1, 3, 2]) -> [2, 2, 2]
def maior_ponta(nums):
  maiorDaPonta = max(nums[0], nums[-1])
  for num in range(0, len(nums)):
    nums[num]= maiorDaPonta
  return nums

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ()
  print ('Maior_ponta')
  test(maior_ponta([1, 2, 3]), [3, 3, 3])
  test(maior_ponta([11, 5, 9]), [11, 11, 11])
  test(maior_ponta([2, 11, 3]), [3, 3, 3])
  test(maior_ponta([11, 3, 3]), [11, 11, 11])
  test(maior_ponta([3, 11, 11]), [11, 11, 11])
  test(maior_ponta([2, 2, 2]), [2, 2, 2])
  test(maior_ponta([2, 11, 2]), [2, 2, 2])
  test(maior_ponta([0, 0, 1]), [1, 1, 1])
  
if __name__ == '__main__':
  main()
