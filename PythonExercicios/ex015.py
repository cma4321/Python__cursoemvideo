kmRodados = int(input('Digite a quantidade de KM rodados:'))
dias = int(input('Digite a quantidade de dias alugado:'))
preço = (dias*60) + (kmRodados*0.15)
print('O valor total para alugar o veículo será de {} reais!'.format(preço))