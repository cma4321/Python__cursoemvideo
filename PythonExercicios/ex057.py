sexo = str(input('Digite seu genero [M/F]:')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados Inválidos, tente novamente informar seu sexo:'))
print('Sexo {} registrado com sucesso'.format(sexo))