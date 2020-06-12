# List Comprehension

# my_list = [0, 1, 2, 3, 4]

# Aqui eu digo que para cada item na minha lista eu quero add o item x, nesse caso x ainda nao tem valor, mas vamos
# ver exemplos a seguir. O range 5 gera 5 indices de numeros crescentes: 0, 1, 2, 3, 4
test = [x for x in range(5)]
print(test)

test = [x*2 for x in range(5)]  # Aqui ja podemos ver que cada x é multiplicado por 2
print(test)

test = [x**2 for x in range(5)]  # Aqui ja podemos ver que cada x é elevado a 2
print(test)

test2 = [x for x in range(11) if x % 2 == 0]  # Podemos tambem colocar condições dentro, nesse caso pegamos só n par
print(test2)
print()


# Vamos supor que queremos arrumar um monte de nomes em uma lista que estao desformatados:
pessoas_sem_formatacao = [' Ana ', 'Manuela', ' felipe', 'PEDRO']
print(pessoas_sem_formatacao)

pessoas_formatadas = [pessoa.strip().capitalize() for pessoa in pessoas_sem_formatacao]
print(pessoas_formatadas)
