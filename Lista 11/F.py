# F. busca
# Verifique quantas ocorrências de uma palavra há numa frase
# frase = 'ana e mariana gostam de banana'
# palavra = 'ana'
# busca ('ana e mariana gostam de banana', 'ana') == 4
def busca(frase, palavra):
  quantidadePalavras, frase=0, frase.split(" ")
  for palavraFrase in frase:
    for numeroLetras in range(0, len(palavraFrase)-len(palavra)+1):
      if palavraFrase[numeroLetras:(len(palavra)+numeroLetras)]==palavra:
        quantidadePalavras+=1
  return quantidadePalavras

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
  test(busca('ana e mariana gostam de banana', 'ana'), 4)
  test(busca('uma arara ou duas araras', 'ara'), 4)

if __name__ == '__main__':
  main()
