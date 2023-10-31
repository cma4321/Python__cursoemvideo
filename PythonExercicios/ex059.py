import math

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite segundo número:"))
opcao = 0
while opcao != 5:
    print("""
    [1] - somar
    [2] - multiplicar
    [3] - maior
    [4] - novos números
    [5] - sair do programa""")
    opcao = int(input("Qual é sua opção?"))

    if opcao == 1:
        total = num1+num2
        print("{} + {} = {}".format(num1,num2,total))
    elif opcao == 2:
        total = num1 * num2
        print("{} * {} = {}".format(num1, num2, total))
    elif opcao == 3:
        if num1 > num2:
            print("{} é maior que {}".format(num1,num2))
        else:
            print("{} é maior que {}".format(num2,num1))
    elif opcao == 4:
        num1 = int(input("Digite o novo primeiro número: "))
        num2 = int(input("Digite o novo segundo número:"))
        print("Os novos números é {} e {} ".format(num1,num2))
    elif opcao == 5:
        exit()

