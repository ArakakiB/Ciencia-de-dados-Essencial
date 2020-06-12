def divisao(n1, n2):
    if n2 == 0:
        return
    return n1/n2


x = divisao(8, 2)  # Só coloquei na variavel para nao precisar escrever divisao() dentro do print

if x:
    print(x)
else:
    print('A funcao retornou none')


