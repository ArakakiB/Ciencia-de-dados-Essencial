my_string = 'o rato roeu a roupa do rei de roma'
tam_string = len(my_string)
nova_string = ''

cont = 0

qtd_vezes_letra = 0
contagem_atual = 0
letra = ''

while cont < tam_string:

    qtd_vezes_letra = my_string.count(my_string[cont])

    if contagem_atual < qtd_vezes_letra and my_string[cont].strip():  # o strip remove os espaços
        letra = my_string[cont]
        contagem_atual = qtd_vezes_letra

    # print('{1} {0}'.format(qtd_vezes_letra, my_string[cont]))

    cont += 1

print(letra, contagem_atual)



