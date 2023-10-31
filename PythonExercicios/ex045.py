from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''
Suas Opções:
[1] - Pedra
[2] - Papel
[3] - Tesoura
''')
jogador = int(input('Qual sua jogada?'))
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)
if computador == 0: # computador escolheu PEDRA
    if jogador == 0: #jogador escolheu PEDRA
        print('EMPATE')
    elif jogador == 1: #jogador escolheu PAPEL
        print('JOGADOR VENCEU!')
    elif jogador == 2: #jogador escolheu TESOURA
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1: # computador escolheu PAPEL
    if jogador == 0: #jogador escolheu PEDRA
        print('COMPUTADOR VENCEU')
    elif jogador == 1: #jogador escolheu PAPEL
        print('EMPATE!')
    elif jogador == 2: #jogador escolheu TESOURA
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2: # computador escolheu TESOURA
    if jogador == 0: #jogador escolheu PEDRA
        print('JOGADOR VENCEU')
    elif jogador == 1: #jogador escolheu PAPEL
        print('COMPUTADOR VENCEU')
    elif jogador == 2: #jogador escolheu TESOURA
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
else:
    print('Opção Inválida')


