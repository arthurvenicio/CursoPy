"""
count - Itertools
"""

from itertools import count

contador = count(start=1, step=2)

for value in contador:
    print(value)

    if value >= 10:
        break
