# Aqui vamos falar sobre formatação

nome = "John"
idade = 24
altura = 1.80
maior_de_idade = idade > 18
peso = 72
imc = peso / (altura ** 2)

# Para escolher a quantidade de casas do numero flutuante é so colocar round(var, 2) OU :.(n)f
print("Olá", nome, "sua idade é", idade, 'anos e seu IMC é de', round(imc, 2))  # Temos essa maneira de escrever, que nao é recomendado
print(f'Olá {nome} sua idade é {idade} anos e seu IMC é de {imc:.2f}')  # Temos essa maneira de escrever, que é mais indicada. NAO ESQUECER DO 'f' no começo
print('Olá {} sua idade é {} anos e seu IMC é de {:.2f}'.format(nome, idade, imc))  # Temos essa maneira de escrever tambem que pode ser util

#                                                                   0      1     2
print('Olá {0} sua idade é {1} anos e seu IMC é de {2:.2f}'.format(nome, idade, imc))  # Aqui sempre sera numerado baseado nos argumentos do .format | Essa é a mais interessante

print('Olá {i} sua idade é {j} anos e seu IMC é de {y:.2f}'.format(i=nome, j=idade, y=imc))  # Aqui podemos tambem chamar a variavel com outra variavel criada no proprio format


