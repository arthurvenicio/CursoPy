# phrase = 'O Brasil participou das olimpiadas, o Brasil foi roubado!'
#
# l1 = phrase.split(' ')
# l2 = phrase.split(',')
#
# for value in l1:
#     print(f'The word {value} appeared {l1.count(value)} times ')

# phrase = 'O Brasil participou das olimpiadas, o Brasil foi roubado!'

# l1 = phrase.split(' ')
# l2 = phrase.split(',')
#
# word = ''
# count = 0
#
# for value in l1:
#     qtd_count = l1.count(value)
#
#     if qtd_count > count:
#         count = qtd_count
#         word = value
# print(f'The word {word} appear {count} times')

phrase = 'O Brasil participou das olimpiadas, o Brasil foi roubado!'
l1 = phrase.split(' ')
l2 = phrase.split(',')


for value in l2:
    print(value.strip().capitalize())