# Uma função é uma sequência de comandos definida com um nome via def. Ela pode ter parâmetros e retornar um valor via return ou yield. Somente é executada quando chamada. return e yield não são funções, apenas palavras reservadas. Também existem lambda funções, mais avançadas.
def f(a):
    a=a+5
    return a
b=0
f(b)
print (b, ',', end = '')
b = f(b)
print (b)
#Saída: 0, 5

#Preencha os quadros segundo a função abaixo
def f(x):
    print ('x', end = '')
    if x <= 1:
        return 1
    else:
        return x + f(x-1)
f(1)
#Saída:x
f(2)
#Saída:xx
f(3)
#Saída:xxx
f(4)
#Saída:xxxx

#Preencha os quadros segundo a função abaixo
def comum(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

comum('azul', 'amarelo')
#Saída: ['a', 'l']

comum(range(5),[1,3,5])
#Saída:[1, 3]

comum('azul',['a','b'])
#Saída:['a']

#Variáveis globais não são alteradas dentro de funções, a menos que declaradas como global dentro delas.
a = 'X'
def func( ):
    a = "O"
func( )
print (a)
#Saída:X

a = 'X'
def func( ):
    global a
    a = 'O'
func( )
print (a)
#Saída:O
