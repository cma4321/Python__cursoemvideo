num = int(input('Digite um numero inteiro:'))
tot = 0
for i in range (1, num +1):
    if num % i == 0:
        print('\033[34m')
        tot += 1
    else:
        print('\033[m')
    print('{} '.format(i), end='')
print('\n\033O número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO')