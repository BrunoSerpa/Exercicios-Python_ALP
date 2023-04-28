# K. has22 #
# Verifica se na lista de números inteiros aparecem dois 2 consecutivos
# has22([1, 2, 2]) -> True
# has22([1, 2, 1, 2]) -> False
# has22([2, 1, 2]) -> False
def has22(nums):
  numAnt=None
  for num in nums:
    if num == numAnt: return True
    numAnt=num
  return False

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
  test(has22([1, 2, 2]), True)
  test(has22([1, 2, 1, 2]), False)
  test(has22([2, 1, 2]), False)
  test(has22([2, 2, 1, 2]), True)
  test(has22([1, 3, 2]), False)
  test(has22([1, 3, 2, 2]), True)
  test(has22([2, 3, 2, 2]), True)
  test(has22([4, 2, 4, 2, 2, 5]), True)
  test(has22([1, 2]), False)
  test(has22([2, 2]), True)
  test(has22([2]), False)
  test(has22([]), False)
  test(has22([3, 3, 2, 2]), True)
  test(has22([5, 2, 5, 2]), False)
if __name__ == '__main__':
  main()