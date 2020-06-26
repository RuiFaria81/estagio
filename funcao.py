def diz_ola(name, age):
    print("Olá " + name + ". Tu tens " + str(age) + " anos de idade.")

def espaco():
    print("======================")


def filhos(*filhos):
    print("O filho mais velho é " + filhos[0])

def filhos_v2(filho3, filho2, filho1):
    print("O filho mais velho é " + filho1)

def nomes(**nome):
    print("O seu último nome é " + nome["ultimo_nome"])

def nacionalidade(pais = "português"):
  print(" ->Eu sou " + pais)

def alimentacao(comida):
  for x in comida:
    print(x)

def retorna(x):
    return 5 * x

def vazia():
    pass


diz_ola("Joao", 32)

espaco()

diz_ola("Francisca", 22)

espaco()

filhos("Francisca", "Pedro", "Miguel")

espaco()

filhos_v2(filho1 = "Francisca", filho2 = "Pedro", filho3 = "Miguel")

espaco()

nomes(primeiro_nome = "Rui", ultimo_nome = "Faria")

espaco()

nacionalidade("suéco")
nacionalidade("índiano")
nacionalidade()
nacionalidade("brasileiro")

espaco()

frutas = ["pêra", "banana", "laranja"]
alimentacao(frutas)

espaco()

print(retorna(4))


