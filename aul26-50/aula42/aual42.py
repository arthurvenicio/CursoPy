# Dictionary Comprehension
lista = [
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
]

d1 = {x.capitalize(): y for x, y in lista}
d2 = {f'chave_{x}': x*2 for x in range(5)}
print(d2)