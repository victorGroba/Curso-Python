a = 'Jose'
b = 'Pedro'
c = 22

string = 'b={nome1} a={nome2} a={nome1} c={nome1}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)