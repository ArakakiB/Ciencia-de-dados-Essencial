"""
Entrada de dados do usuário

A funçao input sempre retorna uma string, independete do que o usuario colocar como dado
"""
ano_atual = 2019

nome = input("Como você gostaria de ser chamado? ")
print('Bem vindo ao sistema {0}'.format(nome))

idade = input("Qual sua idade, {0}? ".format(nome))
# idade = int(input("Qual sua idade, {0}? ".format(nome))) #  Poderia tambem converter antes do input
print('Ok, você nasceu em: {0}'.format(ano_atual - int(idade)))



