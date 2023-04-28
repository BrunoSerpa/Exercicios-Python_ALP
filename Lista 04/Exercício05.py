#5) Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras “python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para minúsculas e de remover antes os caracteres especiais.
texto = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.".lower()

palavrasTexto = texto.split(" ")
quantidadePalavras=0

for palavra in palavrasTexto:
    palavra = ''.join(filter(str.isalnum, palavra)).lower()
    for letra in palavra:
        if letra in "python" and len(palavra)>4:
            quantidadePalavras+=1
            break

print(f'''No texto abaixo:
________________________________________________________________________
    {texto}
________________________________________________________________________
Existem {quantidadePalavras} palavras com uma das letras de python e com mais de 4 letras
''')