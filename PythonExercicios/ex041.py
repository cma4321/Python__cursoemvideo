from datetime import date
atual = date.today().year

ano = int(input('Digite o ano de nascimento:'))
idade = atual - ano

if idade <= 9:
    print('Você tem {} anos e sua categoria é MIRIM'.format(idade))
elif idade >= 10 and idade <= 14:
    print('Você tem {} anos e sua categoria é INFANTIL'.format(idade))
elif idade >= 15 and idade <= 19:
    print('Você tem {} anos e sua categoria é JUNIOR'.format(idade))
elif idade >= 20 and idade <= 25:
    print('Você tem {} anos e sua categoria é SÊNIOR'.format(idade))
else:
    print('Você tem {} anos e sua categoria é MASTER'.format(idade))