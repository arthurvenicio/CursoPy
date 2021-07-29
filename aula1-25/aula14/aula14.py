name = input('Username: ')

caracter_qtd_user = len(name)
ctr_qtd_user = name.__len__()

if caracter_qtd_user > 3:
    psw = input('Password: ')
    caracter_qtd_psw = len(psw)
    if caracter_qtd_psw >= 8:
        print('You have been successfully registered!')
    else:
        print(f'You must type more than 8 characters, you have {caracter_qtd_psw}')
else:
    print('You must type more than 3 characters')
