# Iterando str com while
#       # 012345678910
# nome = 'José Victor'     # str são iteráveis

# tamanho_nome = len(nome)
# print(tamanho_nome)

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1
novo_nome = novo_nome + '*'
print(novo_nome)
print(len(nome))
