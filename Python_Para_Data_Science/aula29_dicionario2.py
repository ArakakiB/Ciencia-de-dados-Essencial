# Da para colocar dicionario dentro de dicionario

clientes = {
    'cliente1': {
        'nome': 'Luiz',
        'sobrenome': 'Otavio',
    },
    'cliente2': {
            'nome': 'Henrique',
            'sobrenome': 'Miranda',
    }

}

print(clientes)
print()

# Percorrendo dicionarios dentro de dicionarios
for k, v in clientes.items():
    print(k)
    for dados_k, dados_v in v.items():
        print(dados_k, dados_v)




