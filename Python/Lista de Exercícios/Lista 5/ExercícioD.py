#Daniela é uma pessoa muito supersticiosa. Para ela, um número é sortudo se ele contém o dígito 2 mas não o dígito 7. Então, na opinião dela, quantos números sortudos existem entre 18644 e 33087, incluindo os extremos?
Numeros, numerosSortudo= 0, 0

for numeros in range(18644, 33087):
    Numeros += 1
    sorte=False
    for numero in str(numeros):
        
        #Caso seja 7
        if int(numero)==7:
            sorte=False
            break
        
        #Caso seja 2
        elif int(numero)==2:
            sorte=True
    
    #Quantidade de Números Sortudos
    if sorte==True:
        numerosSortudo += 1
print (f'Entre 18644 a 33087 existem {Numeros} números, sendo {numerosSortudo} deles, números sortudos (De acordo com Daniela).')