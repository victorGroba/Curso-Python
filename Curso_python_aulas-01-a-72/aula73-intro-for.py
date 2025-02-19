# # texto  = 'Python'


# # i = 0

# # tamanho_string = len(texto)

# # while i < tamanho_string:
# #     print(texto[i], end = ' ') #python por padrao, quebra a linha no looping, esse trecho evita essa quebra de linha
# #     i+=1

# #     #por padrao end é definido por "\n", logo quando definimos end =' ' ele deixa de quebrar a linhas a cada looping


# senha_salva = '2122'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(repeticoes)
# print('Aquele laço acima pode ter  repetições infinitas')

texto = 'Python'

novo_texto = ' '
for letra in texto:  #eu crio uma variavel letra para iterar a variavel texto  
    
    novo_texto += f'*{letra}'
    print(letra)

