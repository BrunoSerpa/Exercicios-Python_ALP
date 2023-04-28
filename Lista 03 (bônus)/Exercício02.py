#2) Indique como um troco deve ser dado utilizando - se um número mínimo de notas. Seu algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado desprezando os centavos. Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que nenhuma delas esteja em falta no caixa.
troco=int(input('Digite quanto deverá ser dado de troco \nResposta:'))

notasDe50, notasDe20, notasDe10, notasDe5, notasDe2, moedaDe1Real = 0, 0, 0, 0, 0, 0
while troco>0:
    if troco>=50:
        troco=troco-50
        notasDe50=notasDe50+1
    elif troco>=20:
        troco=troco-20
        notasDe20=notasDe20+1    
    elif troco>=10:
        troco=troco-10
        notasDe10=notasDe10+1
    elif troco>=5:
        troco=troco-5
        notasDe5=notasDe5+1
    elif troco>=2:
        troco=troco-2
        notasDe2=notasDe2+1
    else:
        troco=troco-1
        moedaDe1Real=moedaDe1Real+1

necessárioParaTroco='Será necessário: '
if notasDe50>0:
    if notasDe50==1:
        necessárioParaTroco=necessárioParaTroco+'uma nota de 50 reais;\n'
    else:
        necessárioParaTroco=necessárioParaTroco+str(notasDe50)+' notas de 50 reais;\n'
if notasDe20>0:
    if notasDe20==1:
        necessárioParaTroco=necessárioParaTroco+'uma nota de 20 reais;\n'
    else:
        necessárioParaTroco=necessárioParaTroco+str(notasDe20)+' notas de 20 reais;\n'
if notasDe10>0:
    necessárioParaTroco=necessárioParaTroco+'uma nota de 10 reais;\n'
if notasDe5>0:
    necessárioParaTroco=necessárioParaTroco+'uma nota de 5 reais;\n'
if notasDe2>0:
    if notasDe2==1:
        necessárioParaTroco=necessárioParaTroco+'uma nota de 2 reais;\n'
    else:
        necessárioParaTroco=necessárioParaTroco+str(notasDe2)+' notas de 2 reais;\n'
if moedaDe1Real>0:
    necessárioParaTroco=necessárioParaTroco+'uma moeda de 1 real.'
print(necessárioParaTroco)