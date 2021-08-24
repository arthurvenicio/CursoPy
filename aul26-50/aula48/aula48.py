from itertools import groupby, tee
from dados import alunos

ordenacao = lambda item: item['nota']
alunos.sort(key=ordenacao)
alunos_agrupados = groupby(alunos, ordenacao)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)

    print(f'Agrupamento: {agrupamento}')

    for aluno in va1:
        print(f'\t{aluno}')

    quantidade = len(list(va2))
    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}')
    print()
