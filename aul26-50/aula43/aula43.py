import sys

# Check size of generator
l1 = (x for x in range(1000))
l2 = [x for x in range(1000)]

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))


# print(next(l1))
# print(next(l1))
# print(next(l1))
# print(next(l1))
# print(next(l1))
# print(next(l1))


# def gera():
#     n = 'text1'
#     yield n
#     n = 'text2'
#     yield n
#     n = 'text3'
#     yield n
#
#
# g = gera()
#
# for v in g:
#     print(v)