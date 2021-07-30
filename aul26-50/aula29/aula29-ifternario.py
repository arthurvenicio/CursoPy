
idade = input('Who old are you? ')

if not idade.isnumeric():
    print('Please enter only number\'s')
else:
    idade = int(idade)
    eh_maior = (idade >= 18)

    msg = 'É de maior' if eh_maior else 'É de menor'

    print(msg)
