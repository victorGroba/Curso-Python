# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5
#Otávio
# -6-5-4-3-2-1
#nome = 'Otávio'
#imprimir(nome[2])
#imprimir(nome[-4])
# print('vio' em nome)
# print('zero' no nome)
#imprimir(10 * '-')
# print('vio' não está em nome)
# print('zero' não está no nome)

nome  =  input ( 'Digite seu nome: ' )
encontrar  =  input ( 'Digite o que deseja encontrar: ' )

if  encontrar  in  nome :
    print ( f' { encontrar } está em { nome } ' )
else :
    print ( f' { encontrar } não está em { nome } ' )