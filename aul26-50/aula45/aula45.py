"""
Zip - unindo interaveis
Zip_longest - Itertools

"""

from itertools import zip_longest, count

indice = count()

cidades  = ['São Paulo', 'Fortaleza', 'Salvador', 'Recife']

estados = ['SP', 'CE', 'BA']

cidades_estados = zip(estados, cidades, indice)

print(list(cidades_estados))