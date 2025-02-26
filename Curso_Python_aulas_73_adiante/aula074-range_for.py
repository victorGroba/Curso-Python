#range ja é uma variável reservado em pyh=thon

#range -> range(start, stop, step)

# numeros = range(0, 10) # ate 10
# numeros = range(5, 10) # de 5 ate 10
# numeros = range(5, 10, 2 )  # de 5 ate 10 de 2 em 2




#todos os números pares de 0 a 100
import time
cont = 0
numeros = range(0, 100, 2)
for numero in numeros:
    cont+=1
    time.sleep(0.1)
    print('⌛' + str(numero), end='\r')
    
 
print('✅Pronto')