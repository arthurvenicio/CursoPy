name = input('What is your name? ')
age = input('How old are you? ')

age = int(age)
if age >= 18:
    print(f'{name} can take a loan!')
else:
    print(f'{name} can\'t take a loan')
