perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 1x1?',
        'respostas': {'a': '1', 'b': '5', 'c': '1.5'},
        'resposta_certa': 'a'
    },

    'Pergunta 2': {
        'pergunta': 'Quanto é 1x5?',
        'respostas': {'a': '1', 'b': '5', 'c': '1.5'},
        'resposta_certa': 'b'
    },

    'Pergunta 3': {
        'pergunta': 'Quanto é 1x10?',
        'respostas': {'a': '1', 'b': '5', 'c': '10'},
        'resposta_certa': 'c'
    }
}

respostas_certas = 0
for qk, qv in perguntas.items():
    print('{0}: {1}'.format(qk, qv['pergunta']))
    print('Respostas:')

    for ak, av in qv['respostas'].items():
        print('{0}: {1}'.format(ak, av))

    user_answer = input('Sua resposta: ')

    if user_answer == qv['resposta_certa']:
        print('Resposta Correta')
        respostas_certas += 1
    else:
        print('Errrrou!')

qntd_perguntas = len(perguntas)
percentual_respostas = respostas_certas / qntd_perguntas * 100

print('Você acertou {0} pergunta(s).'.format(respostas_certas))
print('Voce acertou {0:.2f}% das perguntas.'.format(percentual_respostas))

















