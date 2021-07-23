# num1 = input('Insert an number: ')
# num2 = input('Insert an number: ')
#
# if num1.isnumeric() and num2.isnumeric():
#     num1 = int(num1)
#     num2 = int(num2)
#
#     print(num1 + num2)
# else:
#     print('Please insert only numbers')

num1 = input('Insert an number: ')
num2 = input('Insert an number: ')

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('Please insert only numbers')