#4) Seja ostatement sobre diversidade: “The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.”. Gere uma lista de palavras deste texto com split(), a seguir crie uma lista com as palavras que começam ou terminam com uma das letras “python”. Imprima a lista resultante. Não se esqueça de remover antes os caracteres especiais e cuidado com maiúsculas e minúsculas.
texto = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."

palavrasTexto = texto.split(" ")
palavrasDesejadas=[]

for palavra in palavrasTexto:
    palavra = ''.join(filter(str.isalnum, palavra)).lower()
    for letra in palavra:
        if palavra[0] in "python" or palavra[-1] in "python":
            palavrasDesejadas+=[palavra]
            break

print(f'''No texto abaixo:
________________________________________________________________________
    {texto}
________________________________________________________________________
As palavras do texto com a primeira ou última letra igual a uma das letras da palavra "python" são:
{palavrasDesejadas}
''')