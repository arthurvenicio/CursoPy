print()
print('Jogo de pergunta e respostas!')

perguntas = {
    'Pergunta1': {
        'pergunta': 'Quanto é 4+4?',
        'respostas': {'a':'2','b':'8','c':'12'},
        'resposta_certa': 'b',
    },
    'Pergunta2': {
        'pergunta': 'Quanto é 8+4?',
        'respostas': {'a':'2','b':'8','c':'12'},
        'resposta_certa': 'c',
    },
    'Pergunta3': {
        'pergunta': 'Quanto é 9/3?',
        'respostas': {'a':'3','b':'6','c':'9'},
        'resposta_certa': 'a',
    },
    'Pergunta4': {
        'pergunta': 'Quanto é 4*4?',
        'respostas': {'a':'2','b':'16','c':'12'},
        'resposta_certa': 'b',
    },
    'Pergunta5': {
        'pergunta': 'Quanto é 32+4?',
        'respostas': {'a':'36','b':'48','c':'64'},
        'resposta_certa': 'a',
    },
    'Pergunta6': {
        'pergunta': 'Quanto é 4³?',
        'respostas': {'a':'62','b':'48','c':'64'},
        'resposta_certa': 'c',
    }
}

print()
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Alternativas: ')

    for rk, rv in pv['respostas'].items():
        print(f'{rk}: {rv}')

    resposta_user = input('Qual a opção correta?: ')

    if resposta_user == pv['resposta_certa']:
        print('Uhuuu')
        respostas_certas += 1
    else:
        print('Puxaaa! Você errou :/')

    print()

qtd_perguntas = len(perguntas)
porcentagem = respostas_certas / qtd_perguntas * 100

print()
print(f'Você acertou {respostas_certas} questões')
print(f'Obteve {porcentagem:.2f}% questões')
