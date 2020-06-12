'''
insert - insere um item no indice que quisermos , se eu inserir no indice 0, ele vao 'empurrar'
os outros para frente, o antigo 0 sera 1, o antigo 1 sera 2, e assim por diante
pop - Podemos tambem retirar um item usando o comando 'pop'
del - Deleta/retira varios itens de uma vez
min e max - pegam o primeiro e ultimo indice
range - nos ajuda a criar uma lista sem colocar todos os numeros de 1 a 9.
'''

# insert
list1 = ['A', 52, 'g']
print("")
print(list1)

list1.insert(0, 'Outra coisa')
print(list1)

# pop
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2.pop(0)
list2.pop()  # sem nenhum valor retira o ultimo indice
print("")
print(list2)

# del
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del(list3[2:4])
print("")
print(list3)

# min, max e range
list4 = list(range(1, 10))  # Cria de 1 a 9
print("")
print(list4)
print(max(list4))
print(min(list4))
