""" Tipo tupla é uma lista imutavel """

nomes = ['maria', 'Helena', 'Luiz']
nomes[1] = 'outros'
_,_,nome, *resto = nomes
print(nomes)
print(nome)
