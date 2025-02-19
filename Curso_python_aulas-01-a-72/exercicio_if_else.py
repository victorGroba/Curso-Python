valor_1 = input('Digite um número: ')
valor_2 = input ('Digite outro número: ')

int_valor_1 = int(valor_1)
int_valor_2 = int(valor_2)


if int_valor_1 < int_valor_2:
    print(
        f'{valor_2} é maior que o primeiro valor '
        f'ao que {valor_1}'
    )
else:
    print('Primeiro número é maior')