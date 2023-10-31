r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triangulo')
    if r1 == r2 == r3:
        print('É um triangulo EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('É um triangulo ESCALENO')
    else:
        print('É um triangulo ISÓSCELES')
else:
    print('Os segmentos acima não podem formar um triangulo')