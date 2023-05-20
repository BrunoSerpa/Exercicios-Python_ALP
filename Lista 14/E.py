# Dada uma frase, você deve retirar todas as letras repetidas das palavras e ordenar as letras que sobraram.
# Exemplo: 'ana e mariana gostam de banana' vira 'an e aimnr agmost de abn'
# Dicas: tente transformar cada palavra em um conjunto, depois tente ordenar as letras e montar uma string com o resultado. Utilize listas auxiliares se facilitar
def cripto(frase):
  novapalavra = novafrase = ""
  for letra in frase:
    if letra==" ":
      novafrase+=''.join(sorted(novapalavra)) + " "
      novapalavra=""
    elif not letra in novapalavra: novapalavra += letra
  return novafrase+''.join(sorted(novapalavra))

def test(obtido, esperado):
  if obtido == esperado: prefixo = ' Parabéns!'
  else: prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))

test(cripto('ana e mariana gostam de banana'), 'an e aimnr agmost de abn')
test(cripto('Batatinha quando nasce esparrama pelo chão'), 'Bahint adnoqu acens aemprs elop choã')