# É Par ou impar?

n1 = input("Digite um numero decimal: ")
n2 = input("Digite outro numero decimal: ")

try:
    n1 = int(n1)
    n2 = int(n2)

    print(n1 + n2)

    n1 = n1 % 2
    n2 = n2 % 2

    if n1 == 0 and n2 == 0:
        print('O resultado da soma é PAR')
        print('Seu resultado é um numero inteiro')
    elif n1 != 0 and n2 != 0:
        print('O resultado da soma é PAR')
        print('Seu resultado é um numero inteiro')
    else:
        print('O resultado da soma é IMPAR')
        print('Seu resultado é um numero inteiro')
except:
    print('Erro! Digite apenas numeros inteiros')
