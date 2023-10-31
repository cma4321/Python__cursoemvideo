valor_casa = float(input('Digite o valor da casa:'))
salario = float(input('Digite seu salario:'))
anos = int(input('Em quantos anos você vai pagar?'))
prestação = valor_casa / (anos*12)
if prestação >= (salario*1.3):
    print('Empréstimo Recusado! Valor da prestação mensal acima de 30% do salário')
else:
    print('Empréstimo Aprovado!')