#yield é um gerador, podemos utilizá-lo em uma função onde cada elemento é gerado online via next()
def fat():
    n = 1
    f = 1
    while True:
        f = f * n
        yield f
        n = n + 1
a = fat()
for i in range(5):
    print (next(a), end = ' ')
#Saída: 1 2 6 24 120 

def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b
a = fib()
for i in range(5):
    print (next(a), end = ' ')
#Saída: 1 1 2 3 5