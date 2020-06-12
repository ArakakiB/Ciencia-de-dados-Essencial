'''
lambda
'''

variavel = lambda x, y: x * y
print(variavel(2, 2))
print()

# Vamos fazer um exemplo para ordenar uma lista

lista_0 = [42, 6, 62, 5, 9, 52, 43, 0]
lista_0.sort()  # Ordena automaticamente na ordem crescente
print(lista_0)
print()


# Primeiro vamos fazer criamos a lista com outras listas
lista = [
    ['P1', 13],
    ['P2', 50],
    ['P3', 12],
    ['P4', 35],
    ['P5', 20]
]


# Aqui como temos listas dentro de uma lista, pirmeiro temos que retornar o indice da lista que queremos com a lambda

lista.sort(key=lambda item: item[1], reverse=True)  # item 1 é o indice das sublistas
# fazendo lista.sort, nós alteramos a raiz da lista, ou seja, ela foi alterada definidamente
print(lista)
print()

# Para só printarmos os valores alterados sem alterar a raiz, façamos o seguinte:
print(sorted(lista, key=lambda i: i[1]))  # Eu poderia usar reverse tambem, mas nao quis, nesse caso por padrao é False