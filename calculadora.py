comando = "2"

while comando != "3":

    if comando == "2":
        try:
            num1 = float(input("Introduza um número: "))
        except:
            print("Valor inválido")
            break
        try:
            num2 = float(input("Introduza outro número: "))
        except:
            print("Valor inválido")
            break

        try:
            operacao = int(input("1 -> Adição\n2 -> Subtração\n3 -> Multiplicação\n4 -> Divisão\n  -> "))
        except:
            print("Valor inválido")

        if operacao > 4:
            print("Valor inválido")
            break

        resultado = 0

        if operacao == 1:

                resultado = num1 + num2
                print(str(resultado))

        elif operacao == 2:

                resultado = num1 - num2
                print(str(resultado))

        elif operacao == 3:

                resultado = num1 * num2
                print(str(resultado))

        elif operacao == 4:

                resultado = num1 / num2
                print(str(resultado))


    if comando == "1":
        try:
            numadd = float(input("Adicione outro número: "))
        except:
            print("Valor inválido")

        try:
            operacao = int(input("1 -> Adição\n2 -> Subtração\n3 -> Multiplicação\n4 -> Divisão\n  -> "))
        except:
            print("Valor inválido")

        if operacao > 5:
            print("Valor inválido")
            break

        resultado = 0

        if operacao == 1:

            resultado = num1 + num2
            print(str(resultado))

        elif operacao == 2:

            resultado = num1 - num2
            print(str(resultado))

        elif operacao == 3:

            resultado = num1 * num2
            print(str(resultado))

        elif operacao == 4:

            resultado = num1 / num2
            print(str(resultado))

    comando = input("1 -> Adicionar outro número\n2 -> Limpar a calculadora\n3 -> Terminar\n  -> ")
