carros = ["Ford", "Tesla", "Volvo"]

for x in carros:
    print(x)

carros.append(input("\nIntroduza uma marca de carro\n ->"))

print("\n")

for x in carros:
    print(x)

#ULTIMO CARRO
resposta_remove = input("\nDeseja remover o último carro guardado?\n ->")

if resposta_remove == "sim":
    carros.reverse()
    carros.pop(0)
    carros.reverse()
    print("\n")
    for x in carros:
        print(x)


#CARRO ESPECIFICO
resposta_remove = input("\nDeseja remover algum carro específico?\n ->")

if resposta_remove == "sim":
    for x in carros:
        print(x)
    carro_remove = input("\nQual carro deseja remover\n ->")
    carros.remove(carro_remove)
    for x in carros:
        print(x)










