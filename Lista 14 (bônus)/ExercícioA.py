""" Variáveis, operadores e expressões
As variáveis possuem um tipo, que pode ser verificado
através da função type(x). Você pode converter dados
por meio de funções: int(x), str(x), float(x), bool(x). Elas
darão erro algumas vezes quando não houver sentido
na conversão, por exemplo, int("abacate"). """
a=5
b=a+7
a=10
print (b)
#Saída: 12
print (type(0))
#Saída: <class 'int'>
print (type(0.0))
#Saída: <class 'float'>
print (type(3.14))
#Saída: <class 'float'>
print (type('Py'))
#Saída: <class 'str'>
print (type(True))
#Saída: <class 'bool'>
print (type(1/2))
#Saída: <class 'float'>
print (type(1//2))
#Saída: <class 'int'>
print (type(3**3))
#Saída: <class 'int'>
print (type(0==0))
#Saída: <class 'bool'>
print (type(3<0))
#Saída: <class 'bool'>
print (type(3!=3))
#Saída: <class 'bool'>

print (type(str(int(3.14159265358979))))
#Saída: <class 'str'>

print(3 == 3.0)
#Saída: True
print(1/3)
#Saída: 0.33333333333333333333333333333333333333333333333
print(1//3)
#Saída: 0
print(3 == '3')
#Saída: False
print ('x' != 'x')
#Saída: True
print (2//1)
#Saída: 2
print (not False)
#Saída: True
print (not True)
#Saída: False
print (not 0)
#Saída: True

print (True and (False or not True))
#Saída: False

a = 20
print (15-(a-15), end = ' ')
a = 10
print (15-(a-15), end = ' ')
#Saída:10 20

a = 12.75
print (a - int(a), end = ' ')
a = int((a - int(a))*100)
print (a)
#Saída: 0.75 75

a = 3
b = 4
a = a + b
b = a - b
a = a - b
print (a, b)
#Saída: 4, 3

print (3 % 2)
#Saída:1
print (0 % 2)
#Saída:0
print(123%356254)
#Saída:123

print(type([1, 2]))
#Saída: <class 'list'>
print(type({1:2}))
#Saída: <class 'dict'>
print(type([]))
#Saída: <class 'list'>

a='abacate'
print('e' in a, 'x' in a, end =' ')
print('ate' in a, end =' ')
print('' in a, end =' ')
print('eta' in a, end =' ')
print('eta' not in a)
#Saída: True False True True False True

a= '0123456789'
print(a[0], a[3], a[-1], end = ' ')
print(a[0:3], a[3:6], a[6:9], end = ' ')
print(a[:3], a[7:], end=' ')
print(a[:9:2], end=' ')
print(a[::-1])
#Saída: 0 3 9 012 345 678 012 789 02468 9876543210

a = [1, 2, [3, 4]]
print (1 in a, end = ' ')
print ([1, 2] in a, end = ' ')
print ([3, 4] in a, end = ' ')
print (3 in a, end = ' ')
print (3 in a[2], end = ' ')
print (5 not in a)
#Saída: True False True False True True

a = {1: 'ab', 2: 'cd', 'x':3.14}
print (1 in a, 3 in a, end=' ')
print ('x' in a, 'z' in a, end=' ')
print (a[1], a['x'])
#Saída: True False True False ab 3.14