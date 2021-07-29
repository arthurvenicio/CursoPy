name = input('What is your name? ')
crt_name = len(name)

if crt_name <= 4:
    print('Your name is short!')
elif 5 <= crt_name <= 6:
    print('Your name is normal!')
else:
    print('Your name is big')
