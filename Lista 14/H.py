# H. Anagrama
# Verifique se duas palavras são anagramas,
# isto é são uma é permutação das letras da outra
# anagrama('aberto', 'rebato') = True
# anagrama('amor', 'ramo') = True
# anagrama('aba', 'baba') = False
def anagrama(s1, s2):
  return sorted(s1)==sorted(s2)

def test(obtido, esperado):
  if obtido == esperado: prefixo = ' Parabéns!'
  else: prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))

test(anagrama('abacate', 'abacatx'), False)
test(anagrama('sim', 'xxs'), False)
test(anagrama('sim', 'siiimmmmm'), False)
test(anagrama('iracema', 'america'), True)
test(anagrama('ator', 'rota'), True)
test(anagrama('aberto', 'rebato'), True)
test(anagrama('amor', 'roma'), True)
test(anagrama('ramo', 'amor'), True)
test(anagrama('baba', 'aba'), False)
test(anagrama('casa', 'cassa'), False)
test(anagrama('palmeiras', 'abacate'), False)
test(anagrama('alegria', 'alergia'), True)
test(anagrama('cantiga', 'catinga'), True)