'''
split - divide uma string. divide e transforma em uma lista
join -
enumerate -
'''

string = "O Brasil é o país do futebol, o Brasil é penta!"
lista = string.split(' ')  # Ele vai separar somente onde achar espaço, eliminando o espaço. Poderia ser qualquer letra

print(lista)

# Aqui ele conta para mim quantas vezes cada palavra aparece na lista
for item in lista:
    print(item, lista.count(item))

