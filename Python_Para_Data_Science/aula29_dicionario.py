d1 = {'chave1': 'valor da chave', 'chave2': 'Outro valor'}
d2 = dict(chave1='Valor da chave', chave2='Outra chave')  # Podemos criar assim tambem
d3 = {1: 'valor da chave', 2: 'Outro valor'}

d1['nova_chave'] = 'Valor novo'  # Para adicionarmos/atualizarmos valores no dicionario
del d1['chave2']

print(d1)
print(d2)
print(d3)
print()
print(d1['chave1'])
print(d3[2])
print(len(d3))  # Conta quantos pares tem no dicionario
print()

# Verificando se existe o valor

print('chave1' in d1)  # Verifica a se a chave existe
print('valor da chave' in d1.values())  # Verifica se o valor existe
print()

var1 = 'chave1' in d1

print(var1)

if var1:
    print("Existe")
else:
    print("nao existe")

print()
# Percorrendo um dicionario

for i in d3:  # Traz somente as chaves
    print(i)

for i in d3.values():  # Traz somente os valores das chaves
    print(i)

for i in d3.items():  # Traz chave e valor
    print(i)

for k, v in d3.items():  # Poderia usar assim tambem para usar as variaveis de maneira independente
    print(k, v)



