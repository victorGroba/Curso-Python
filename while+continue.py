contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostraro número 6')
        continue
    
    if contador >= 10 and contador <= 27:
        print('Não vou mostraro o', contador)
        continue

    print(contador)

    if contador == 40:
        break
print('Acabou') 