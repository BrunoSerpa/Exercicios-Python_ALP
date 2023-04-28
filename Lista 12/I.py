# I. inicio_final
# Divida cada string em dois pedaços.
# Se a string tiver um número ímpar de caracteres
# o primeiro pedaço terá um caracter a mais,
# Exemplo: 'abcde', divide-se em 'abc' e 'de'.
# Dadas 2 strings, a e b, retorna a string
# a_inicio + b_inicio + a_final + b_final
def inicio_final(a, b):
  aInicio, aFinal= (a[0:int(len(a)/2)] , a[int(len(a)/2):len(a)]) if len(a)%2==0 else (a[0:int(len(a)/2)+1] , a[int(len(a)/2)+1:len(a)])
  bInicio, bFinal= (b[0:int(len(b)/2)] , b[int(len(b)/2):len(b)]) if len(b)%2==0 else (b[0:int(len(b)/2)+1] , b[int(len(b)/2)+1:len(b)])
  return f'{aInicio}{bInicio}{aFinal}{bFinal}'

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))

def main():
  test(inicio_final('abcd', 'xy'), 'abxcdy')
  test(inicio_final('abcde', 'xyz'), 'abcxydez')
  test(inicio_final('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
