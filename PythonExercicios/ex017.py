import math

CA = int(input('Digite o valor do cateto adjascente:'))
CO = int(input('Digite o valor do cateto oposto: '))
hipotenusa = math.hypot(CA, CO)
print('O valor da hipotenusa é {}'.format(hipotenusa))