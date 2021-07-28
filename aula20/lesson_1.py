while True:
    print()
    num1 = input('Insert an number: ')
    num2 = input('Insert another number: ')
    operator = input('Insert the operator ')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Insert a number valid')
        continue

    num1 = int(num1)
    num2 = int(num2)

    if operator == '+':
        print(num1 + num2)
    elif operator == '-':
        print(num1 + num2)
    elif operator == '/':
        print(num1 / num2)
    elif operator == '*':
        print(num1 * num2)
    else:
        print('Insert a operator valid')
        z

    leave = input('You should leave? [Y]es or [N]o ? ')
    if leave == 'y':
        break
