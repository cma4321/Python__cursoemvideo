import math

valor = float(input('Digite o valor do angulo:'))
sen = math.sin(math.radians(valor))
cos = math.cos(math.radians(valor))
tan = math.tan(math.radians(valor))

print('O seno do angulo de {} é {:.2f}, seu cosseno é {:.2f}, e sua tangente é {:.2f}'.format(valor,sen,cos,tan))