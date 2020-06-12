'''
quando criamos uma função que nao sabemos qual a quantidade de argumentos vamos precisar, utilizamos a palavra *args
colocamos essa palavra para indicar que vamos ter uma quantidade indefinida de argumentos, nesse caso conseguimos
acessar normalmente os valores como uma lista/string, porem, serao tuplas, ou seja, nao podem ser modificadas
Para conseguir alterar os valores de uma tupla, temos que transforma-la em lista. Para isso faremos o cast
Obs: a unica diferença da tupla para a lista é que nao se pode alterar os valores, isso significa que tudo que vimos
para lista se aplica a tupla, com excessao de alteração de valores

Temos tambem o **kwargs, que são argumentos com palavras. Se eu colocar uma string, como por exemplo: nome = 'ronaldo'
ele nao vai printar na tela, porque qualquer atribuição que é feita depois dos argumentos passados na funcao da erro
para isso usamos o kwargs, que serve para aceitar esse tipo de argumento. Exemplos a baixo...
'''


def func(*args, **kwargs):
    args = list(args)  # Aqui transformo o args tupla em args lista. Agorap posso alterar valores
    args[1] = 30
    print(args)
    print(args[0])
    print(len(args))

    print(kwargs)
    print(kwargs['nome'], kwargs['snome'])

    print()
    # Poderia acessar assim tambem:
    var_qualquer = kwargs['nome']
    print(var_qualquer)

    # Podemos acessar tambem assim:
    variavel_qualquer = kwargs.get('idade')  # Se eu colocar um argumento valido, ele printa, se nao, nao.
    if variavel_qualquer:
        print()
        print(variavel_qualquer)
    else:
        print()
        print('Nao foi possivel achar o valor')


func(1, 2, 3, nome='rolando', snome='nunes')
