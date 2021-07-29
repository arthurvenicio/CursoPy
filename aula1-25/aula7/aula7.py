name = 'Arthur'
age = 19
height = 1.71
legal_age = age > 18
weight = 69.9
bmi = weight / (height ** 2)

print(f'{name}, have {age} old and your BMI is {bmi:.2f}')
print('{}, have {} old and your BMI is {:.2f}'.format(name, age, bmi))
print('{n}, have {a} old and your BMI is {b:.2f}'.format(n=name, a=age, b=bmi))
