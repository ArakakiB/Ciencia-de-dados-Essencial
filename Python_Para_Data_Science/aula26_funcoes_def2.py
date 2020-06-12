'''
Por padrao, uma função sempre retorna um valor, se nao colocarmos para retornar algo, ele retorna o valor none
o valor none em python tem valor, nesse caso é não valor (0 ou False)
podemos retornar qualquer tipo de variavel, lista

'''


def funcao(var):  # O 'var' pode ser qualquer variavel, entao qualquer que eu passo chamando a função, ele aceita
    return var
    # Qualquer coisa depois do return nao é executado


# Só coloquei na variavel x para nao precisa ficar escrevendo funcao(10) dentro do print a baixo
x = funcao(10)  # Pode ver que aqui o Pycharm já avisa que a funcao nao retorna valor

if x:
    print(x)
else:
    print('Sem valor')

