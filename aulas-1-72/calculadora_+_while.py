# Calculadora Exercício

while True: 
    numero_1 = input('Digite um numéro: ')
    numero_2 = input('Digite outro numéro: ')
    operador = input('Digite um operador (+-*/): ')

    numeros_validos = None
    numero_1_float = 0
    numero_2_float = 0
    
    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados não são válidos.  ')
        continue

    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos:
        print('Operador digitado não é válido.  ')
        continue
    
    if len(operador) > 1:
            print('Digite apenas um operador.  ')
            continue
    
    print('Realizando sua conta, confira o resultado a baixo. ')
    if  operador == '+':
        print( f'{numero_1_float}+{numero_2_float}=', numero_1_float + numero_2_float)
    elif operador ==  '-':
        print( numero_1_float - numero_2_float)
    elif operador ==  '/':
        print( numero_1_float / numero_2_float)
    elif operador == '*':
        print( numero_1_float * numero_2_float)
    else:
        print('Nunca deveria chegar aqui. ')
        
    
    sair = input('Quer sair [s]im ').lower().startswith('s')
    
    if sair is True:
        print('Caculadora encerrada. ')
        break