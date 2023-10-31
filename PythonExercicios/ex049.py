tabuada = int(input('Escolha a tabuada:'))
for n in range (0, 11):
    soma = tabuada*n
    print('{} x {} = {}'.format(tabuada,n,soma))
print('FIM')