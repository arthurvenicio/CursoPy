variable = 'value'


def func():
    print(variable)


def func_2(arg=None):
    arg = arg.replace('v', 'c')
    return arg


func()
another_variable = func_2(arg=variable)
print(another_variable)
