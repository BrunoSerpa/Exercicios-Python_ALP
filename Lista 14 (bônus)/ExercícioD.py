#Laços dentro de laços. Determine bem os comandos do bloco de cada laço. break e continue se aplicam ao laço do seu bloco apenas. Aponte loops infinito caso ocorra.
""" 
a=0
while a < 3:
    while True:
        print ('X', end = ' ')
        break
    print ('O', end = ' ')
    a=a+1
#Saída:X O X O X O

a=1
while a < 3:
    while a < 3:
        print ('O', end = ' ')
    a=a+1
#Saída: Loop infinito

a=1
while a < 3:
    if a % 2 == 0:
        b=1
        while b < 3:
            print ('X', end = ' ')
            b=b+1
    print ('O', end = ' ')
    a=a+1
#Saída: O X X O

a=1
while a < 3:
    b=1
    while b < 3:
        if a == 2:
            print ('X', end = ' ')
        print ('O', end = ' ')
        b=b+1
    print ('O', end = ' ')
#Saída: Loop infinito

x = 'abacate'
while x:
    print (x, end = ' ')
    x = x[1:]
#Saída:abacate bacate acate cate ate te e

x = 10
while x:
    x = x - 1
    if x % 2 != 0:
        continue    
    print (x, end = ' ')
#Saída:8 6 4 2 0

while 1:
    nome = input('Nome:')
    if nome == 'fim': break
    print ('Bom dia ', nome)
#Saída: Bom dia  nomeDigitado
"""
x = 'python'
achou = False
vogal = 'aeiou'
while x and not achou:
    if x[0] in vogal:
        print ('X', end = ' ')
        achou = True
    else:
        x = x[1:]
    if not achou:
        print ('O', end = ' ')
#Saída: O O O O X