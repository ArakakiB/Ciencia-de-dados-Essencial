'''
Funções
criamos a funcao com def
podemos passar parametros/argumentos para a funcao OU nao, se nao quisermos, como é o caso da 'funcao'
na 'funcao' criamos a função e depois chamamos ela em outro lugar do programa
Observe em 'def saudacao', que dentro de parenteses nos enviamos 2 parametros, sao eles 'msg e nome'
poderiamos deixar sem valor a 'msg' e 'nome', e deveriamos preencher na chamada da função, porem, coloquei um valor em
cada para exemplificar que podemos colocar um valor padrao. Se nao colocarmos esse valor, obrigatoriamente quando
chamarmos essa função, será necessário passar um parametro
'''

def funcao():
    print('Ola Python')


def saudacao(msg='Olá', nome='Usuário'):
    print(msg, nome)


funcao()
saudacao()
saudacao('Eae!', 'Fulaninho de tal')
saudacao(nome='Siclaninho')  # Se quisermos passar uma parametro fora de ordem, é só dizer qual parametro é

