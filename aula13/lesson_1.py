user = input('Username: ')
password = input('Password: ')

db_user = 'arthur'
db_password = '12345'

if user == db_user and password == db_password:
    print('You are logged!')
else:
    print('Credentials don\'t match')
