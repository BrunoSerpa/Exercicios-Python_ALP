# H. end_other #
# as duas strings devem ser convertidas para minúsculo via lower()
# depois disso verifique que no final da string b ocorre a string a
# ou se no final da string a ocorre a string b
# end_other('Hiabc', 'abc') -> True
# end_other('AbC', 'HiaBc') -> True
# end_other('abc', 'abXabc') -> True
def end_other(a, b):
  if len(a)>len(b):
    return a[len(a)-len(b):len(a)].lower()==b.lower()
  else:
    return b[len(b)-len(a):len(b)].lower()==a.lower()

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
  test(end_other('Hiabc', 'abc'), True)
  test(end_other('AbC', 'HiaBc'), True)
  test(end_other('abc', 'abXabc'), True)
  test(end_other('Hiabc', 'abcd'), False)
  test(end_other('Hiabc', 'bc'), True)
  test(end_other('Hiabcx', 'bc'), False)
  test(end_other('abc', 'abc'), True)
  test(end_other('xyz', '12xyz'), True)
  test(end_other('yz', '12xz'), False)
  test(end_other('Z', '12xz'), True)
  test(end_other('12', '12'), True)
  test(end_other('abcXYZ', 'abcDEF'), False)
  test(end_other('ab', 'ab12'), False)
  test(end_other('ab', '12ab'), True)
if __name__ == '__main__':
  main()