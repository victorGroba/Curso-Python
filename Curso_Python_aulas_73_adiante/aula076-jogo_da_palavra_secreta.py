palavra_secreta =  'deus'
letras_acertadas = ''

cont = 0

while True:
    letra_digitada = input('Digite uma letra: ')

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue

    print('Vamos')

    if letra_digitada in palavra_secreta:
       letras_acertadas += letra_digitada
       

    print(letras_acertadas)

    for letra_secreta in palavra_secreta:
        print(letra_secreta)