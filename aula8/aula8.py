
name = 'Arthur'
age = 19
height = 1.71
weight = 69
year = 2021
born_year = year - age
bmi = weight / height ** 2

print(f'{name}\'s {age} old, your height is {height} and your weight is {weight}')
print(f'{name}\'s BMI is {bmi:.2f}')
print(f'{name} born in {born_year}')
