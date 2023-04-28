a = 1
while a < 10:
 print ('X', end = ' ') 
#Saída: X X X X X X X [...]

a = -1
while a < 3:
 print ('X', end = ' ')
 a = a + 1
#Saída: X X X X

while False: print ('X', end = ' ')
#Saída: Não sairá nada

a = 5
b = 9
while a <= b:
 print ('X', end = ' ')
 if a % 2 == 0: print ('O', end = ' ')
 a = a + 1
#Saída: X X O X X O X

a=1
while a % 7 != 0:
 if a % 2 == 0: print ('O', end = ' ')
 if a == 2: print ('X', end = ' ')
 a=a+1
#Saída:O X O O

#Cuidado com pequenas mudanças de código...
repete = True
a=0
b=0
while repete:
    print ('O', end = ' ')
    a=a+5
    b=b+7
    if a + b >= 24:
        repete = False
#Saída: O O

repete = True
a=0
b=0
while repete:
    print ('O', end = ' ')
    if a + b >= 24:
        repete = False
    a=a+5
    b=b+7
#Saída: O O O

repete = True
a=0
b=0
while repete:
 print ('O', end = ' ')
 if a + b > 24:
    repete = False
 a=a+5
 b=b+7
#Saída: O O O O