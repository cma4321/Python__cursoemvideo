peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura:'))
IMC = peso / (altura ** 2)

if IMC < 18.5:
    print('IMC = {:.2f} e  você está Abaixo do peso'.format(IMC))
elif IMC >= 18.5 and IMC < 25:
    print('IMC = {:.2f} e você está no PESO IDEAL'.format(IMC))
elif IMC >= 25 and IMC < 30:
    print('IMC = {:.2f} e você está SOBREPESO'.format(IMC))
elif IMC >= 30 and IMC < 40:
    print('IMC = {:.2f} e você está OBESO'.format(IMC))
else:
    print('IMC = {:.2f} e você está com OBESIDADE MÓRBIDA'.format(IMC))