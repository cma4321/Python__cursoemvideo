distancia = float(input('Digite a distância da viagem:'))

if distancia >= 200:
    preço = distancia*0.45
else:
    preço = distancia*0.5

print('O valor total de uma viagem de {} Km é de R$ {}'.format(distancia,preço))