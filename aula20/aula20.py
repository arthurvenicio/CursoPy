"""
While
"""

# x = 0
# while x < 10:
#     if x == 3:
#         x = x + 1
#         continue
#     print(x)
#     x = x + 1
#
# print('Acabou!')

# x = 0
# while x < 10:
#     if x == 3:
#         x = x + 1
#         break
#     print(x)
#     x = x + 1
#
# print('Acabou!')

x = 0  # Column
while x < 10:
    y = 0  # Line
    while y < 5:
        print(f'({x},{y})')
        y += 1
    x += 1

print('Acabou!')
