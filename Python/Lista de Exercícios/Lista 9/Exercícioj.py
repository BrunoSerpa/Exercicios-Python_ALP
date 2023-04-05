# J. alarm_clock #
# day: 0=domingo, 1=segunda, 2=terça, ..., 6=sábado
# vacation = True caso você esteja de férias
# o retorno é uma string que diz quando o despertador tocará
# dias da semana '07:00'
# finais de semana '10:00'
# a menos que você esteja de férias, neste caso:
# dias da semana '10:00'
# finais de semana 'off'
# alarm_clock(1, False) -> '7:00'
# alarm_clock(5, False) -> '7:00'
# alarm_clock(0, False) -> '10:00'
def alarm_clock(day, vacation):
  if 6>day>0 and vacation or not vacation:
    if 6>day>0 and not vacation:
      return '7:00'
    return '10:00'
  return 'off'

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
  print ('Alarm Clock')
  test(alarm_clock(1, False), '7:00')
  test(alarm_clock(5, False), '7:00')
  test(alarm_clock(0, False), '10:00')
  test(alarm_clock(6, False), '10:00')
  test(alarm_clock(0, True), 'off')
  test(alarm_clock(6, True), 'off')
  test(alarm_clock(1, True), '10:00')
  test(alarm_clock(3, True), '10:00')
  test(alarm_clock(5, True), '10:00')

if __name__ == '__main__':
  main()
