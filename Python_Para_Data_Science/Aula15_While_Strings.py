my_string = 'o rato roeu a roupa do rei de roma'
tam_string = len(my_string)
nova_string = ''

print(my_string.count('a'))  # Conta quantas vezes a letra 'a' apareceu na string

cont = 0

"""
Nesse while fazemos a nova_string adquirir caracteres da my_string, só que mudando os 'r' minusculos para maiusculos
Vale lembrar que uma string é imutavel, por isso mesmo que mudemos ela depois, a raiz dela ainda é a que foi criada primeiro
por isso fizemos esse exercicio
"""
while cont < tam_string:

    if my_string[cont] == 'r':
        nova_string += my_string[cont].upper()
    else:
        nova_string += my_string[cont]

    cont += 1

print('{0}'.format(nova_string))