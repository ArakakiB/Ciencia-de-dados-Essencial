'''
Indice e Fatiamento de strings
'''

# indices positivos        012345678
texto =                   "Python sz"
# indices negativos       -987654321
# Perceba que nos indices negativos começamos do -1, porque é o primeiro n negativo

print(texto[5])  # Imprimi a letra n, porque é o 5º caractere do indice
print(texto[-4])  # Imprimi a letra n, porque esta no indice -4

print(texto[2:6])  # Pega de um indice ao outro, aqui perceba que o ultimo indice é onde corta, o 6 nao aparece
print(texto[:6])  # Posso fazer assim tambem para pegar tudo que bem antes do 6
print(texto[7:])  # E possso fazem asssim tambem para pegar tudo após o 7

print(texto[0:8:2])  # aqui é igual antes, só que no ultimo ' : ' eu digo de quanto em quanto ele vai pular as casas
print(texto[0::2])







