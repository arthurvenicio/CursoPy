from random import randint

number = randint(100000000, 999999999)

number = str(number)

novo_cpf = number

# Counters
reverso = 10
total = 0

for i in range(19):
    if i > 8:
        i -= 9

    total += int(novo_cpf[i]) * reverso

    reverso -= 1

    if reverso < 2:
        reverso = 11

        det = 11 - (total % 11)

        if det > 9:
            det = 0
        total = 0
        novo_cpf += str(det)

print(novo_cpf)
