salario = float(input('Qual seu salario?'))

if salario > 1250:
    reajuste = salario + (salario*0.1)
    print('Seu salario com reajuste de 10% é de {}'.format(reajuste))
if salario <= 1250:
    reajuste = salario + (salario*0.15)
    print('Seu salario com reajuste de 15% é de {}'.format(reajuste))