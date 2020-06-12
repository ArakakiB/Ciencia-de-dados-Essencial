'''
split - divide uma string. divide e transforma em uma lista
join - junta uma lista
enumerate - enumera elementos de uma lista
'''

string = "O Brasil é penta!"
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor)

