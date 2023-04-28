# G. count_code #
# conta quantas vezes aparece 'code'
# a letra 'd' pode ser trocada por outra qualquer
# assim 'coxe' ou 'coze' também são contadas como 'code'
# count_code('aaacodebbb') -> 1
# count_code('codexxcode') -> 2
# count_code('cozexxcope') -> 2
def count_code(s):
  coe=0
  for n in range(0, len(s)-3):
    coe+=1 if (s[n:n+2]=='co' and s[n+3]=='e') else 0
  return coe

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
  test(count_code('aaacodebbb'), 1)
  test(count_code('codexxcode'), 2)
  test(count_code('cozexxcope'), 2)
  test(count_code('cozfxxcope'), 1)
  test(count_code('xxcozeyycop'), 1)
  test(count_code('cozcop'), 0)
  test(count_code('abcxyz'), 0)
  test(count_code('code'), 1)
  test(count_code('ode'), 0)
  test(count_code('c'), 0)
  test(count_code(''), 0)
  test(count_code('AAcodeBBcoleCCccoreDD'), 3)
  test(count_code('AAcodeBBcoleCCccorfDD'), 2)
  test(count_code('coAcodeBcoleccoreDD'), 3)
if __name__ == '__main__':
  main()