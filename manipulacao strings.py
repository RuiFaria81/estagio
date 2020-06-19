frase = "Bom Dia,\n Tudo bem?"
numero = 20
numero_string = "22"
print(frase)

print("\n\n" + frase + "\n  - Sim, está tudo bem.")

print("\n")

print(str(numero))

print(int(numero_string))

print("\n")

unir = frase + numero_string

print(unir)

print("\n")


unir2 = frase + " 123456 " + numero_string

print(unir2)

print("\n")




numitem = 222
preco = 9.95
encomenda = "Eu quero encomendar o item número {} por {} euros."
print(encomenda.format(numitem, preco))


print("\n")


print(frase.lower())
print("\n" + frase.upper())

print("\n")


print(frase.isupper())
print(frase.upper().isupper())

print("\n")

print(len(frase))

print("\n")
print(frase[12])

print("\n")

print(frase.index("Bom"))

print("\n")

print(frase.replace("bem", "mal"))

print("\n")

#https://www.w3schools.com/python/python_strings.asp