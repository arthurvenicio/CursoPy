num = input('Insert an number: ')

if num.isnumeric():
    num = int(num)

    if num % 2 == 0:
        print('This number is evens')
    else:
        print('This number is odds')
