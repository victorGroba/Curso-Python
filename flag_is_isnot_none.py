# Flag (Bandeira) -  Marcar um local
# None = Não Valor 
# is e is not = é ou não é ( tipo, valor, identidade) 

condição = True
passou_no_if = None

if condição:
    passou_no_if = True
    print('Faça Algo')
else:
    print('Não faça Algo')

print(passou_no_if,passou_no_if is None)
print(passou_no_if,passou_no_if is not  None)

