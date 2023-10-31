n1 = int(input('Digite o primeiro numero:'))
n2 = int(input('Digite o segundo numero:'))
n3 = int(input('Digite o terceiro numero:'))

if n1 > n2 and n1 > n3 and n2>n3:
    print('Maior valor: {} \nMenor Valor: {} '.format(n1,n3))

if n1>n2 and n2<n3:
    print('Maior valor: {} \nMenor Valor: {}'.format(n1,n2))
