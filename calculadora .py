opcao = ""

while opcao != "5":
    print("_" * 40)
    print("| CALCULADORA |")
    print("_" * 40)
    print("1 - Somar dois números")
    print("2 - Subtrair dois números")
    print("3 - Multiplicar dois numeros")
    print("4 - Dividir dois numeros")
    print("5 - Sair")
    print("_" * 40)

    opcao = input("\n Escolha uma opção: ")

    if opcao == "1":
        print("\nVamos fazer uma soma!")
        try:
            num1 = float(input("Entre com o primeiro número: "))
            num2 = float(input("Entre com o segundo número: "))
            print(f"{num1} + {num2} = {num1+num2}")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    elif opcao == "2":
        print("\nVamos subtrair!")
        try:
            num1 = float(input("Entre com o primeiro número: "))
            num2 = float(input("Entre com o segundo número: "))
            print(f"{num1} - {num2} = {num1-num2}")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    elif opcao == "3":
        print("\nVamos Multiplicar!")
        try:
            num1 = float(input("Entre com o primeiro número: "))
            num2 = float(input("Entre com o segundo número: "))
            print(f"{num1} * {num2} = {num1*num2}")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    elif opcao == "4":
        print("\nVamos Dividir!")
        try:
            num1 = float(input("Entre com o primeiro número: "))
            num2 = float(input("Entre com o segundo número: "))
            if num2 != 0:
                print(f"{num1} / {num2} = {num1/num2}")
            else:
                print("Erro: Divisão por zero não é permitida.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    elif opcao == "5":
        print("\nFechando o programa, até mais.")

    else:
        print("\nOpção inválida, tente novamente.")
