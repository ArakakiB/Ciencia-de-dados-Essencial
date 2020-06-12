'''
Em Python não usamos chaves e nem parenteses nos escopos

--- OPERADORES
== igualdade
>  maior que
<  menor que
>= maior ou igual
<= menor ou igual
!= diferente

--- OPERADORES LOGICOS
and = E
or = OU
not = inverso / inverte o resultado
in = existe em
not in = não existe em

'''

a = ''
b = "Beltrano"
senha = int(input('Digite a senha para entrar: '))

if senha == 1234 or senha == 123:
    print('Bem vindo Sr. Fulaninho de tal')
    # Como 'a' não tem valor, o IF verifica se é verdadeiro, como nesse caso não é ele nao deve entrar na condição desse if
    # porem, como temos o not, ele inverte o resultado, entao nesse caso o a é verdadeiro, apesar de na real ser falso
    # no contexto geral estamos dizendo "Se 'a' não tem valor, printe isso"
    if not a:
        print("Preencha um valor para 'a'")
elif senha == 4321:
    print('Bem vindo Sr. Fulano de tal MESTRE')
    if 'tra' in b:
        print('Existe a palavra "tra" na variavel "b"')
    if 'Z' not in b:
        print('Não existe "Z" na variavel "b"')
else:
    print("Senha incorreta --'")




