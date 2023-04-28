#11) Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.
import sys
sys.set_int_max_str_digits(301030)
numero=2**(10**6)
numeroTexto=str(numero)
quantidadeDeDigitos = len(numeroTexto)
print('2 elevado a um milhão tem {} dígitos'.format(quantidadeDeDigitos))