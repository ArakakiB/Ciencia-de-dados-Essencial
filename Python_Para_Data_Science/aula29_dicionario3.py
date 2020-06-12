import copy

d1 = {1: 'a', 2: 'b', 3: 'c', 'lista': ['x', 'y', 'z']}

# v = d1  # Se atribuirmos assim, o python não cria um novo dicionario, ele so atribui a variavel ao dicionario
# v = d1.copy()  # Para criar um novo precisarmos fazer dessa maneira
v = copy.deepcopy(d1)  # Para criar um novo efetivo (jeito certo) devemos importar a biblioteca "copy" e usar essa func

v[1] = 'Python'

print(v)

# Acessando uma lista dentro de um dicionario

print(v['lista'][0])  # Acesso a chave 'lista' no indice 0
print()

# Provando como copiamos o dicionario
v['lista'][0] = 'Xis'
print(v['lista'][0])
print(d1['lista'])

# Obs:
# Conseguimos tambem transformar listas com pares em dicionario
# No dicionario tambem temos as funcoes pop Ex: d1.pop[2]
# Conseguimos tambem adicionar um dicionario ao outro usando o update Ex. d1.update(d2)



