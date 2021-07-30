# list = ['Dan', 'Mortiz', 'Leo']
#
# start_with_M = False
#
# for value in list:
#     if value.lower().startswith('m'):
#         start_with_M = True
#
# if start_with_M:
#     print('We have one name starting with M')
# else:
#     print('We have\'nt a name staring with M')

list = ['Dan', 'Mortiz', 'Leo']


for value in list:
    if value.lower().startswith('m'):
        print('We have one name starting with M')
        break
else:
    print('We have\'nt a name staring with M')
