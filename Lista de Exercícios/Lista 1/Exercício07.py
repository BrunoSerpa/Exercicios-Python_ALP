#07) Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32
Temperatura= float(input('Insira uma temperatura (em °C)\nresposta:'))
grausFahrenheit =  Temperatura * 1.8 + 32
print('{}°C é igual a {}°F'.format(Temperatura, grausFahrenheit))