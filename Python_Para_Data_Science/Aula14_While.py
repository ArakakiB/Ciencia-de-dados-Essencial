x = 0
while x <= 5:

    if x == 3:
        x = x + 1
        #  continue  # O "continue" vai para o prox laço, quando o python ler o continue, ele vai ignorar o cod de baixo
        break  # O "break" sai do laço
    print(x)
    x += 1  # isso é igual a x = x + 1
else:
    print("Finish")

print("Finish")

'''
Em python, tambem é posivel usar o else no while
Nesse caso, o else só é ativado se o while for falso, observe que deixei o break ativo, isso significa que o
while é true, mas foi quebrado o laço do while no meio do caminho, por isso nao foi executado o else
'''

