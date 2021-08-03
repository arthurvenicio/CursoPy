def func(*args, **kwargs):
    print(*args, sep='-')

    age = kwargs.get('age')

    if age is not None:
        print(age)
    else:
        print('Don\'t have age here!')


list = [1, 2, 3, 4, 5]

func(*list, age=31)
