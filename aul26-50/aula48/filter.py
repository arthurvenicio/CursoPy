from dados import pessoas

new_list = filter(lambda x: x['idade'] >= 15, pessoas)

new_list = list(new_list)

print(new_list)
