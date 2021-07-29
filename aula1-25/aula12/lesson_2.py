name = input('What is your name? ')
age = input('How old are you? ')

age = int(age)
min_age = 20
max_age = 30

if age >= min_age and age <= max_age:
    print(f'{name} can take a loan!')
else:
    print(f'{name} can\'t take a loan')
