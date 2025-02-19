senha_correta = 2002
senha = None

while senha != senha_correta:
    senha = input("Digite a senha: ")
    int_senha = int(senha)
    if int_senha == senha_correta:
        print('Acesso permitido')
    else:
        print(f'Senha invalida: {int_senha}')
    break

        