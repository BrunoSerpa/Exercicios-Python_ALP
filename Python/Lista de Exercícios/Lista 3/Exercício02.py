#2) Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
while True:
    nome=input('Insira o nome do usuário \nResposta:')
    senha=input('Insira a senha do usuário \nResposta:')
    if nome!=senha:
        break
    else:
        print('Sua senha está igual ao nome do usuário, tente novamente!! \n\n')