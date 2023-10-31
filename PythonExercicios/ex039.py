from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano de seu nascimento:'))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento,idade,atual))
if idade < 18:
    qntfalta = 18 - idade
    print('Fique tranquilo, sua hora de se alistar vai chegar, falta {} anos'.format(qntfalta))
elif idade == 18:
    print('Já está na hora de se alistar ao serviço militar!')
else:
    qntpassou = idade - 18
    print('Já passou da hora de se registrar ao serviço miltiar, você está atrasado {} anos '.format(qntpassou))