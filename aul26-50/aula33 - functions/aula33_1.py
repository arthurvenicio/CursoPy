# def funcao():
#     print('Teste')
#
# funcao()

# def funcao(msg):
#     print(msg)
#
# funcao('Hello!')

# def funcao(msg, name):
#     print(msg, name)
#
# funcao('Hello', 'Arthur')

# def funcao(msg='Bom dia', name='Doutor'):
#     print(msg, name)
#
# funcao(name='Arthur')

def saudacao(msg='Boa tarde', name='Doutor'):
    return f'{msg} {name}'

variavel = saudacao()

print(variavel)
