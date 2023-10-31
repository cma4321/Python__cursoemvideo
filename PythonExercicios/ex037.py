numero = int(input('Digite um numero inteiro:'))
print('''Escolha uma das bases para conversão:
[1] - Binário
[2] - Octal
[3] - Hexadecimal''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)))

elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)))

elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)))
else:
    print('Opção Inválida!')