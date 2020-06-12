'''
Formatando valores com modificadores

:s - texto (string)
:d - inteiro (int)
:f - Nums flutuantes (float)
:.(número)f - qntd de casas decimais (float)
:(caractere)(> ou < ou ^)(qntd)(tipo - s, d ou f)

> - esquerda
< - direita
^ - centro
'''

n1 = 11
n2 = 3
divisao = n1 / n2
nome = 'John Doe'

print('{}'.format(divisao))  # sem formatação
print('{:.2f}'.format(divisao))  # com formatação dizendo que quero 2 casas flutuantes
print(f'{divisao:.2f}')  # Com 'f string'

# Quero que complete com o '0' a direita até 10 caracteres (os caracteres da variavel contam)
# pode ser qualquer caractere no lugar do 0
# Ele conta as casas apos a virgula
# Ele conta tambem o ponto do ponto flutuante como caractere
# Não consegui colocar mais de 1 caractere
print('{:0<10}'.format(n1))
print('{:0^10}'.format(n1))
print('{:S>3}'.format(n1))
print('{:X>6.2f}'.format(n1))

# outra maneira de fazer, só que com as funções do python
print(nome.rjust(20, 'Z'))
print(nome.ljust(20, 'X'))

# e de brinde formatações de maiusculo, minusculos e maiusculo na primeira letra
print(nome.upper())
print(nome.lower())
print(nome.title())

