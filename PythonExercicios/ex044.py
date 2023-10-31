valor = float(input('Qual é o valor da compra?'))
print('''[1] - A vista/Cheque'
         [2] - A vista no cartão
         [3] - Em até 2x no cartão
         [4] - Em 3x ou mais no cartão''')
pagamento = int(input('Qual é o método de pagamento?'))
if pagamento == 1:
    valor = valor - (valor*0.1)
    print('O valor da compra com 10% de desconto fica R$ {}'.format(valor))
elif pagamento == 2:
    valor = valor - (valor*0.05)
    print('O valor da compra com 5% de desconto fica R$ {}'.format(valor))
elif pagamento == 3:
    valor = valor/2
    print('O valor da compra fica R$ {} por 2 meses'.format(valor))
elif pagamento == 4:
    valor = valor + (valor*0.2)
    print('O valor total da compra fica R$ {}'.format(valor))
else:
    print('OPÇÃO INVÁLIDA! Tente novamente!')