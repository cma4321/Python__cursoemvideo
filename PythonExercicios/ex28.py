import random

num = random.randint(0,5)
NumUsuario = int(input('Escolha um numero de 0 a 5:'))
if NumUsuario == num:
    print('Parabéns, você adivinhou!')
else:
    print('Poxa, você errou. Tente Novamente!')
    print('O número que você tinha que escolher era {}'.format(num))


