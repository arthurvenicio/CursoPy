cart = []

cart.append(('Produto1', 30))
cart.append(('Produto2', 30))
cart.append(('Produto3', 40))

total = sum([float(x[1]) for x in cart])
print(cart)
print(total)