# Faça um programa que peça ao usuário para digitar um número inteiro,
# informe se este número é par ou ímpar. Caso o usuário não digite um número
# inteiro, informe que não é um número inteiro.

# numero = input('Digite um número inteiro: ')  # ISDIGIT --> Função para saber se input é um número

# if numero.isdigit(): 
#     numero_int = int(numero)
#     par_impar = numero_int % 2 == 0
#     ar_impar_texto = ' ímpar'

#     if par_impar is True:
#         par_impar_texto = 'Par'
#     print(f'O número  {numero_int} é {par_impar_texto} ')
# else:
#     print('Você não digitou um número inteiro ')



# # Faça um programa que exige a hora ao usuário e, baseando-se no horário
# # descrito, exiba a saudação correspondente. Ex.
# # Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
    
# entrada = input(' Digite que horas são em números inteiros: ')


# try :
#     hora_int = int(entrada)
    
#     if hora_int >= 0 and hora_int <= 11:
#         print('Bom dia!') 
#     elif hora_int >= 12  and hora_int <= 17:
#         print('Boa tarde!')
#     elif hora_int >= 18  and hora_int <= 23:
#         print('Boa Noite!')
#     else:    
#          print('Não reconheço essa hora')

# except:
#     print('Digite apenas númeroa inteiros')



# Faça um programa que parte do primeiro nome do usuário. Se o nome tiver 4 letras ou
# menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
# “Seu nome é normal”; maior que 6 escreva "Seu nome é muito grande".

nome = input(' Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto.')
    elif tamanho_nome >= 5 and tamanho_nome <=6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito Grande')
else:
    print('Digiti mais de uma letra')
