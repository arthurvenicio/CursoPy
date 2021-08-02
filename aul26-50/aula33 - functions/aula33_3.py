# def welcome(saudacao, name):
#     print(saudacao, name)
#
#
# welcome('Olá', 'Arthur')
#
# def soma(n1, n2, n3):
#     print(n1 + n2 + n3)
#
#
# soma(1, 1, 1)
#
# def acrescimo(n1, n2):
#
#     n2 = n1 * (n2 / 100)
#
#     return n1 + n2
#
#
# discount = acrescimo(30, 25)
#
# print(discount)

def fizzbuzz(var):

    divpor3 = (var % 3 == 0)
    divpor5 = (var % 5 == 0)

    if divpor3 and divpor5:
        return 'FizzBuzz'
    elif divpor3:
        return 'Fizz'
    elif divpor5:
        return 'Buzz'
    else:
        return var


t = fizzbuzz(3)
e = fizzbuzz(5)
s = fizzbuzz(15)

print(t)
print(e)
print(s)
