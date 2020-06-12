# Colocar o indice em 9 numeros começando pelo dez e seguindo de forma decrescente

lista = list(range(10, 1, -1))

for ind, item in enumerate(lista):
    print(ind, item)

