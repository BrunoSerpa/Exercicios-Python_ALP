# I. count_evens
# conta os números pares da lista
# count_evens([2, 1, 2, 3, 4]) -> 3
# count_evens([2, 2, 0]) -> 3
# count_evens([1, 3, 5]) -> 0
def count_evens(nums):
  par=0
  for num in nums:
    par+=1 if num%2==0 else 0
  return par

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
  test(count_evens([2, 1, 2, 3, 4]), 3)
  test(count_evens([2, 2, 0]), 3)
  test(count_evens([1, 3, 5]), 0)
  test(count_evens([]), 0)
  test(count_evens([11, 9, 0, 1]), 1)
  test(count_evens([2, 11, 9, 0]), 2)
  test(count_evens([2]), 1)
  test(count_evens([2, 5, 12]), 2)
if __name__ == '__main__':
  main()