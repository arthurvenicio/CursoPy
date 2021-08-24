from dados import pessoas


def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20)
    return p


names = map(aumenta_idade, pessoas)

for pessoa in names:
    print(pessoa)