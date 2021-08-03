# # 1 -

# def func(arg):
#     return arg('value')


# def func_2(arg=None):
#     arg = arg.replace('v', 'c')
#     return print(arg)


# func(func_2)


def func(arg, *args, **kwargs):
    return arg(*args, **kwargs)


def func_2(name):
    return f'Oi {name}'


def func_3(name, saudacao):
    return f'{saudacao} {name}' 


exec = func(func_3, 'Arthur', 'Oi')

print(exec)
