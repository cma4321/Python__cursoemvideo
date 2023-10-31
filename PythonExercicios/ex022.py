nome = input('Qual seu nome?')
print(nome.upper()) #poe a frase em maisculo
print(nome.lower()) #poe a frase em minuscula
print(len(nome)-nome.count(' ')) #conta a quantiade de letras sem espaços na frase

dividido = nome.split()
print(dividido[0])
print(len(dividido[0]))