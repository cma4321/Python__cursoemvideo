from random import randint

computador = randint(0, 11)
num = 0
cont = 0;

print("Pensei em um numero de 0 a 11, tente adivinhar")
while num != computador:
    num = int(input("Qual seu palpite?"))
    cont=cont+1
    if num < computador:
        print("Mais.. tente novamente")
    else:
        print("Menos.. tente novamente")
print('''Parabéns, você acertou ao escolher o numero {}
e foi preciso {} tentativas'''.format(num, cont))