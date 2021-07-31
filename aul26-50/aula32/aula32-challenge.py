while True:
    # Catch the cpf
    cpf = input('Insira seu cpf: ')

    # Create new cpf
    novo_cpf = cpf[:-2]

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

    seq = novo_cpf == str(novo_cpf[0]) * len(cpf)
    conditinal = (cpf == novo_cpf)

    # Priting if is valid or not
    msg = 'Valido' if conditinal and not seq else 'Inválido'
    print(msg)
