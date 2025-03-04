# 
# Listas em Python
# Tipo list - Mutável
# Suporta vários valores de qualquer tipo
# Conhecimentos reutilizáveis - índices e fatiamento
# Métodos úteis: append, insert, pop, del, clear, extend, +
# 

lista = [1, 2, 3, 4]

# numero = lista[2]
# lista[2] = 300

#função para apagar item da lista
del lista[0]

#Adcionar itens ao final da lista (método Append)
lista.append(50)

#Remover item da lista (método pop) --> esse metódo retorna algo, entao podemos fazer atribuiçoes
ultimo_valor=lista.pop() ; """remove o ultimo item da lista"""

""" O indice -1 sempre vai ser o ultimo item da minha lista """

# Insert recebe dois argumentos (indice, valor a ser inserido)

lista.insert(0,100)

print(lista)








print(lista, ultimo_valor)