# H. not_bad
# Dada uma string, procura a primeira ocorrência de 'not' e 'bad'
# Se 'bad' aparece depois de 'not' troca 'not' ... 'bad' por 'good'
# Assim 'This dinner is not that bad!' retorna 'This dinner is good!'
def not_bad(s):
  palavras=s.split(" ")
  temNot, quantAntNot=False,0
  for palavra in palavras:
    quantAntNot+=len(palavra)+1 if palavra!="not" and not temNot else 0
    temNot=True if palavra in "not" else temNot
    if palavra[0:2] in "bad" and temNot==True:
      palavra='good'if len(palavra)==3 else 'good'+palavra[3:len(palavra)+1]
      s=s[0:quantAntNot]+palavra
  return s

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))

def main():
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

if __name__ == '__main__':
  main()