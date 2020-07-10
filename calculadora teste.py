
num1 = float(input("Introduza um número: "))
num2 = float(input("Introduza outro número: "))
operacao = input("Qual operação deseja fazer? ")
resultado = 0
numadd = 0

if operacao == "+":

    if resultado == 0:
        resultado = num1 + num2
        print(str(resultado))
    else:
        resultado = resultado + numadd
        print(str(resultado))

elif operacao == "-":

    if resultado == 0:
        resultado = num1 - num2
        print(str(resultado))
    else:
        resultado = resultado - numadd
        print(str(resultado))

elif operacao == "*":

    if resultado == 0:
        resultado = num1 * num2
        print(str(resultado))
    else:
        resultado = resultado * numadd
        print(str(resultado))

elif operacao == "/":

    if resultado == 0:
        resultado = num1 / num2
        print(str(resultado))
    else:
        resultado = resultado / numadd
        print(str(resultado))

comando = input("1 -> Adicionar outro número\n2 -> Limpar a calculadora\n3 -> Terminar\n  -> ")

if comando == 1:
    numadd = float(input("Adicione outro número: "))
    operacao = input("Qual operação deseja fazer? ")
elif comando == 2:
    resultado = 0
    numadd = 0
elif comando == 3:
    print("ola")

