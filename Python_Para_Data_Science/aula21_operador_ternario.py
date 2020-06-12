# Temos essa maneira de fazer, que já conhecemos
'''
login = False

if login:  # lembrando que quando nao colocamos nada para verificar, automaticamente perguntamos se é true
    msg = 'Usuario logado'
else:
    msg = 'Usuario precisa logar'

print(msg)
'''


'''
Agora vamos utilizar o operador ternario para obter o mesmo resultado
'''

login = False

msg = 'Usuario logado' if login else 'Usuario precisa logar'
print(msg)
