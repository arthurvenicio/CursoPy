"""
:s (strings)
:d (Int)
:f  (Float)
:.(number)f - Number of decimal places
:(CHARACTER)(> OR < OR ^)(QUANTITY)(TYPE - s, d or f)

> - LEFT
< - RIGHT
^^- CENTER
"""

# num1 = 10
# num2 = 3
# division = num1 / num2
# print(f'{division:.2f}')

# name = 'Arthur'
# print(f'{name:s}')

# FILLING NUMBERS

# num1 = 1
# print(f'{num1:0>10}')  # NOW THE NUMBER HAVE 10 CHARACTER ON LEFT SIDE
# num2 = 1121
# print(f'{num1:0<10}')  # NOW THE NUMBER HAVE 10 CHARACTER ON RIGHT SIDE
# num1 = 777
# print(f'{num1:0^10}')  # NOW THE NUMBER HAVE 10 CHARACTER ON CENTER

name = "Arthur Venicio"
format_name = '{n:0<20}'.format(n=name)
print(format_name)