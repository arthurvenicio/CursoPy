"""
For in
Iteralçao com for
Função range (start=0, stop, step=1)

"""

# text = 'Javascript'
#
# for letter in text:
#     print(letter)
#
# for n in range(10):
#     print(n)

text = 'Javascript'
nova_string = ''

for letter in text:
    if letter == 't':
        nova_string = nova_string + letter.upper()
    elif letter == 'h':
        nova_string += letter.upper()
    else:
        nova_string += letter

print(nova_string)