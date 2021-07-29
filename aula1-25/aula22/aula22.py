"""
#Iteração
"""


# frase = 'o rato roeu a roupa do rei de roma'
# tamanho_frase = len(frase)
# contador = 0
# nova_string = ''
#
# while contador < tamanho_frase:
#     # print(frase[contador])
#     nova_string += frase[contador]
#     print(nova_string)
#     contador += 1
#
# print(nova_string)

frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

input_do_usuario = input('Qual letra você deseja maiuscula? ')

while contador < tamanho_frase:
    letra = frase[contador]

    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string+= letra
    contador += 1

print(nova_string)
