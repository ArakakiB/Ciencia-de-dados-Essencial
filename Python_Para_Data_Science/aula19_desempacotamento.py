# Como o desempacotamento ocorre...
lista = ['a', 'b', 'c']
n1, n2, n3 = lista
print(n2)
# ... ele pega por indice


'''
O que acontece aqui em baixo, é que se eu tentar desempacotar uma lista que contem mais
itens que variaveis (para guardar o item) o programa da um erro
para isso, podemos criar uma lista (outra_lista) dentro da lista (lista2)
para acomodar o excesso restante de itens
'''
lista2 = ['a', 'b', 'c', 1, 2, 3, 4, 5]
a1, a2, a3, *outra_lista = lista2
print(a1, a2, a3, outra_lista)

'''
o sistema para declarar qual variavel vai pegar qual indice se baseia em:
do lado esquedo da lista criada (outra_lista_b) se tem o 0, 1, 2 como vimos acima
porem, do lado direito pega o indice invertido começando do final, como podemos ver abaixo
e o restante tambem é acomodado na outra_lista_b
'''

lista3 = ['a', 'b', 'c', 1, 2, 3, 4, 5]
*outra_lista_b, b1, b2, b3 = lista3
print(outra_lista_b, b1, b2, b3)
