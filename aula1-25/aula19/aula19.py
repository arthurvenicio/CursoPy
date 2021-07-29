"""
* String indices

https://docs.python.org/3/library/stdtypes.html (Built-in Types)
https://docs.python.org/3/library/functions.html (Built-in Functions)
"""
# Positive
text = "Python s2"
print(text[3])  # Selecionando um indice

# Negative
print(text[-1])
print(text[:-1])

# Pulando Caractere
print(text[0:6:2]) # [ONDE COMEÇA : ONDE TERMINA : QUANTIDADE DE CARACTERE A SER PULADO]

# Fatiando
print(text[2:6])  # Selecionando um trecho
print(text[:6])  # Selecionando do inicio ate um ponto
print(text[7:])  # Selecionando de um trecho até o fim
# or
print(text[0:6])  # Na primeira o zero está omitido

