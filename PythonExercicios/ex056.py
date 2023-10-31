somaidade=0
media = 0
maiorhomem = 0
nomevelho = ''
totmulher = 0
for p in range (1,5):
    print('---- {}* PESSOA ----'.format(p))
    nome = str(input('Digite o nome:')).strip()
    idade = int(input('Digite a idade:'))
    sexo = str(input('Digite o sexo[M/F]:')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorhomem:
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
media = somaidade / 4
print('A media de idade do grupo é {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorhomem,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher))