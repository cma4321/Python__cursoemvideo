nome = str(input('Qual seu nome?'))
if nome == 'Caio':
    print('Que nome bonito!')
elif nome == 'Maria' or 'João':
    print('Seu nome é bem comum no Brasil!')
else:
    print('Seu nome é bem normal')
print("Muito prazer {}".format(nome))