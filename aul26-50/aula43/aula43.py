import sys

l1 = (x for x in range(100))

# print(next(l1))
# print(next(l1))
# print(next(l1))
# print(next(l1))
# print(next(l1))
# print(next(l1))


def gera():
    n = 'text1'
    yield n
    n = 'text2'
    yield n
    n = 'text3'
    yield n


g = gera()

for v in g:
    print(v)