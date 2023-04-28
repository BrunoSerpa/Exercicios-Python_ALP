#O laço for executa o bloco de comandos uma vez para cada elemento de uma sequência.
for x in ['a', 3.14, 7/2]:
    print (x, end = ' ')
#Saída: a 3.14 3.5

s = 0
for x in [7, 2, -2, 5]:
    s = s + x
print (s)
#Saída: 12

p = 1
for x in [1, -1, 2, -2]: p = p * x
print (p)
#Saída: 4

p = 1
for x in 'aeiou':
    print (x*3, end = ' ')
#Saída: aaa eee iii ooo uuu

L = [1, 2, 3, 4, 5]
for x in range(len(L)):
    L[x] += 1
print (L)
#Saída: [2, 3, 4, 5, 6]

for x in 'abc':
    for y in '012':
        print (x + y, end = ' ')
#Saída:a0 a1 a2 b0 b1 b2 c0 c1 c2

L = [1, 7, 4, 12, -2]
x = L[0]
while True:
    L = L[1:]
    if not L:
        break
    if L[0] > x:
        x = L[0]
print (x)
#Saída: 12