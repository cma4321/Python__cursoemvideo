velocidade = float(input('Digite a velocidade do carro:'))
if velocidade >= 80:
    valor = (velocidade-80)*7
    print('Multado! Sua velocidade é de {} km/h e o '
          'limite é 80 km/h, '
          'valor da multa a pagar: {} reais '.format(velocidade,valor))


