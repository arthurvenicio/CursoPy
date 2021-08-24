from dados import pessoas
from functools import reduce

new_list = reduce(lambda ac, p: p['idade'] + ac, pessoas, 0)

print(new_list)
