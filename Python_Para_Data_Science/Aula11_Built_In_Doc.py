n1 = input("Digite um numero decimal: ")
n2 = input("Digite outro numero decimal: ")

# n1 = int(n1)
# n2 = int(n2)

# print(n1 + n2)

'''
Perceba que acima, ele soma os 2 numeros apenas. Porem, se eu digitar no input um numero flutuante ou uma letra por 
exemplo, ele vai dar erro e parar o programa
Para tratar isso e não haver ERRO (que vá travar) no programa temos 2 opçoes nesse momento do curso:
1 - Verificar com a função 'isdigit', 'isnumeric' ou 'isdecimal' em um bloco if
2 - Tratar como excessao um erro geral com o 'try except'
'''
"""Vamos testar a primeira opção logo a baixo e depois a segunda"""

# if n1.isdigit() and n2.isdigit():
#     n1 = int(n1)
#     n2 = int(n2)
#
#     print(n1 + n2)
# else:
#     print("ERROR")

"""E agora vamos testar a segunda opção"""
# É melhor essa opcao, é a mais usada
try:
    n1 = int(n1)
    n2 = int(n2)

    print(n1 + n2)
except:
    print("ERROR")

