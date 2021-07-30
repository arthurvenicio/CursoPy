secret_word = "word"
words = []
chance = 3

while True:
    if chance <= 0:
        print('You wont')
        break

    letter = input('Enter insert an character ')

    if len(letter) > 1:
        print('Enter only one character at a time')
        continue

    words.append(letter)
    if letter in secret_word:
        print(f'Niceee, have {letter} in the secret word')
    else:
        print(f'Ohh, don\'t have {letter} in the secret word')
        words.pop()
        chance -= 1

    secret_temp = ''
    for secret_letter in secret_word:
        if secret_letter in words:
            secret_temp += secret_letter
        else:
            secret_temp += '*'

    if secret_temp == secret_word:
        print('Nice you have the secret word')
        break
    else:
        print(f'You have: {secret_temp}')