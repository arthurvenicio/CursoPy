# a = lambda x, y: x * y

# print(a(2, 2))

# list = [
#     ['P1', 22],
#     ['P2', 8],
#     ['P3', 28],
#     ['P4', 11],
#     ['P5', 66]
# ]
#
#
# def func(item):
#     return item[1]
#
#
# list.sort(key=func)
#
# print(list)

# list = [
#     ['P1', 22],
#     ['P2', 8],
#     ['P3', 28],
#     ['P4', 11],
#     ['P5', 66]
# ]
#
# list.sort(key=lambda item: item[1])
#
# print(list)

list = [
    ['P1', 22],
    ['P2', 8],
    ['P3', 28],
    ['P4', 11],
    ['P5', 66]
]

print(sorted(list, key=lambda i: i[1]))
