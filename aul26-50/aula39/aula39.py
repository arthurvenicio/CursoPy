list = [
    [1,2,3,4,5,6,7,8,9,10],
    [9,1,8,9,9,7,2,1,6,8],
    [1,3,2,2,8,6,5,9,6,7],
    [3,8,2,8,6,7,7,3,1,9],
    [4,8,8,8,5,1,10,3,1,7],
]


# def foundNumb(list):
#     for l in list:
#         checked_numbers = set()
#         first_duplicated = -1
#
#         for v in l:
#             if v in checked_numbers:
#                 first_duplicated = v
#                 break
#
#             checked_numbers.add(v)
#         # return first_duplicated
#
#         print(l, first_duplicated)
#
# foundNumb(list)

def foundNumb(list):

    checked_numbers = set()
    first_duplicated = -1

    for v in list:
        if v in checked_numbers:
            first_duplicated = v
            break

        checked_numbers.add(v)
    return first_duplicated

for l in list:
    print(l, foundNumb(l))

