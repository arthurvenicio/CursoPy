# List Comprehension
tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)

ex = [(y, x) for x, y in tupla]
ex = dict(ex)

print(ex)

l3 = list(range(100))

ex2 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
print(ex2)

# Utilizando o else
ex3 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]

print(ex3)