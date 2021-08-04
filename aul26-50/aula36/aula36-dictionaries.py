# import copy
#
# d1 = {
#     'name': 'Arthur',
#     'age': 19,
#     'city': 'Santa Cruz',
#     'count': [1, 2, 3]
# }
#
# v = copy.deepcopy(d1)
# v['city'] = 'Caruaru'
# v['count'][2] = 5
# print(d1)
# print(v)

d1 = {
    1: 2,
    2: 3,
    3: 4
}

d2 = {
    'a': 'b',
    'b': 'c',
    'c': 'd'
}

d3 = {}

d3.update(d1)
d3.update(d2)

print(d1)
print(d2)
print(d3)

