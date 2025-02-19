int_idade = 0
soma = 0
cont = 0

while int_idade >= 0:
    
    idade = input("Digite sua idade: ")
    int_idade = int(idade)
    if int_idade <= 0:
        continue
    soma += int_idade
    cont += 1

if cont == 0:
    print("Digite um valor válido")
else:
    media = soma / cont
    print(f'A média das idades foi {media}')
    

        

