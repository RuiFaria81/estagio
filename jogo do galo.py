import random

pri = "0"
seg = "1"
ter = "2"
qua = "3"
qui = "4"
sex = "5"
set = "6"
oit = "7"
non = "8"
comando = "0"
empate = 0


jogador = 1

jogo = "| {0} | {1} | {2} |\n| {3} | {4} | {5} |\n| {6} | {7} | {8} |\n"

def menu():
    global comando
    comando = input("---------------MENU---------------\n\n1 -> Iniciar o jogo 1vs1\n2 -> Iniciar jogo contra bot\n3 -> Como jogar\n4 -> Sair\n  -> ")

def como_jogar():
    global comando
    comando = "0"
    print(comando)
    print("\n---------------COMO JOGAR---------------\n")
    chama_jogo()
    print("Tente fazer com que o seu simbolo faça uma linha horizontal, vertical ou diagonal\nPara colocar o seu simbolo basta digitar o numero onde o deseja jogar")

def chama_jogo():
    print (jogo.format(pri, seg, ter, qua, qui, sex, set, oit, non))



def onde_jogar():
    global pri, seg, ter, qua, qui, sex, set, oit, non
    global jogador
    global jogada
    global empate

    jogada = input("Onde deseja jogar? ->")

    if jogador == 1:
        if jogada == "0":
            if pri == "0":
                pri = "x"
                jogador = jogador + 1
                empate = empate + 1
            else:
                print("Esse valor já esta ocupado")
        elif jogada == "1":
            if seg == "1":
                seg = "x"
                jogador = jogador + 1
                empate = empate + 1
            else:
                print("Esse valor já esta ocupado")
        elif jogada == "2":
            if ter == "2":
                ter = "x"
                jogador = jogador + 1
                empate = empate + 1
            else:
                print("Esse valor já esta ocupado")
        elif jogada == "3":
            if qua == "3":
                qua = "x"
                jogador = jogador + 1
                empate = empate + 1
            else:
                print("Esse valor já esta ocupado")
        elif jogada == "4":
            if qui == "4":
                qui = "x"
                jogador = jogador + 1
                empate = empate + 1
            else:
                print("Esse valor já esta ocupado")
        elif jogada == "5":
            if sex == "5":
                sex = "x"
                jogador = jogador + 1
                empate = empate + 1
            else:
                print("Esse valor já esta ocupado")
        elif jogada == "6":
            if set == "6":
                set = "x"
                jogador = jogador + 1
                empate = empate + 1
            else:
                print("Esse valor já esta ocupado")
        elif jogada == "7":
            if oit == "7":
                oit = "x"
                jogador = jogador + 1
                empate = empate + 1
            else:
                print("Esse valor já esta ocupado")
        elif jogada == "8":
            if non == "8":
                non = "x"
                jogador = jogador + 1
                empate = empate + 1
            else:
                print("Esse valor já esta ocupado")


    elif jogador == 2:
        if jogada == "0":
            if pri == "0":
                pri = "o"
                jogador = jogador - 1
                empate = empate + 1
            else:
                print("Esse valor já esta ocupado")
        elif jogada == "1":
            if seg == "1":
                seg = "o"
                jogador = jogador - 1
                empate = empate + 1
            else:
                print("Esse valor já esta ocupado")
        elif jogada == "2":
            if ter == "2":
                ter = "o"
                jogador = jogador - 1
                empate = empate + 1
            else:
                print("Esse valor já esta ocupado")
        elif jogada == "3":
            if qua == "3":
                qua = "o"
                jogador = jogador - 1
                empate = empate + 1
            else:
                print("Esse valor já esta ocupado")
        elif jogada == "4":
            if qui == "4":
                qui = "o"
                jogador = jogador - 1
                empate = empate + 1
            else:
                print("Esse valor já esta ocupado")
        elif jogada == "5":
            if sex == "5":
                sex = "o"
                jogador = jogador - 1
                empate = empate + 1
            else:
                print("Esse valor já esta ocupado")
        elif jogada == "6":
            if set == "6":
                set = "o"
                jogador = jogador - 1
                empate = empate + 1
            else:
                print("Esse valor já esta ocupado")
        elif jogada == "7":
            if oit == "7":
                oit = "o"
                jogador = jogador - 1
                empate = empate + 1
            else:
                print("Esse valor já esta ocupado")
        elif jogada == "8":
            if non == "8":
                non = "o"
                jogador = jogador - 1
                empate = empate + 1
            else:
                print("Esse valor já esta ocupado")


def verifica_empate():
    global empate

    chama_jogo()
    if empate == 9:
        print("O jogo foi empatado")


def verifica_vitoria():
    global pri, seg, ter, qua, qui, sex, set, oit, non
    global jogador
    global empate

    #HORIZONTAL
    if pri == seg and seg == ter:
        if jogador == 2:
            jogador = jogador - 1
        elif jogador == 1:
            jogador = jogador + 1
        print("\n\nO jogador " + str(jogador) + " ganhou")
        empate = 10
    elif qua == qui and qui == sex:
        if jogador == 2:
            jogador = jogador - 1
        elif jogador == 1:
            jogador = jogador + 1
        print("\n\nO jogador " + str(jogador) + " ganhou")
        empate = 10
    elif set == oit and oit == non:
        if jogador == 2:
            jogador = jogador - 1
        elif jogador == 1:
            jogador = jogador + 1
        print("\n\nO jogador " + str(jogador) + " ganhou")
        empate = 10


    #VERTICAl
    if pri == qua and qua == set:
        if jogador == 2:
            jogador = jogador - 1
        elif jogador == 1:
            jogador = jogador + 1
        print("\n\nO jogador " + str(jogador) + " ganhou")
        empate = 10
    elif seg == qui and qui == oit:
        if jogador == 2:
            jogador = jogador - 1
        elif jogador == 1:
            jogador = jogador + 1
        print("\n\nO jogador " + str(jogador) + " ganhou")
        empate = 10
    elif ter == sex and sex == non:
        if jogador == 2:
            jogador = jogador - 1
        elif jogador == 1:
            jogador = jogador + 1
        print("\n\nO jogador " + str(jogador) + " ganhou")
        empate = 10


    #DIAGONAL
    if pri == qui and qui == non:
        if jogador == 2:
            jogador = jogador - 1
        elif jogador == 1:
            jogador = jogador + 1
        print("\n\nO jogador " + str(jogador) + " ganhou")
        empate = 10
    elif set == qui and qui == ter:
        if jogador == 2:
            jogador = jogador - 1
        elif jogador == 1:
            jogador = jogador + 1
        print("\n\nO jogador " + str(jogador) + " ganhou")
        empate = 10

def contra_bot():
    global pri, seg, ter, qua, qui, sex, set, oit, non
    global jogador
    global jogada
    global empate

    jogada = (random.randint(0, 8))

    if jogada == "0":
        if pri == "0":
            pri = "o"
            jogador = jogador - 1
            empate = empate + 1
            print(jogada)
        else:
            jogada = (random.randint(0, 8))
    elif jogada == "1":
        if seg == "1":
            seg = "o"
            jogador = jogador - 1
            empate = empate + 1
            print(jogada)
        else:
            jogada = (random.randint(0, 8))
    elif jogada == "2":
        if ter == "2":
            ter = "o"
            jogador = jogador - 1
            empate = empate + 1
            print(jogada)
        else:
            jogada = (random.randint(0, 8))
    elif jogada == 3:
        if qua == "3":
            qua = "o"
            jogador = jogador - 1
            empate = empate + 1
            print(jogada)
        else:
            jogada = (random.randint(0, 8))
    elif jogada == 4:
        if qui == "4":
            qui = "o"
            jogador = jogador - 1
            empate = empate + 1
            print(jogada)
        else:
            jogada = (random.randint(0, 8))
    elif jogada == 5:
        if sex == "5":
            sex = "o"
            jogador = jogador - 1
            empate = empate + 1
            print(jogada)
        else:
            jogada = (random.randint(0, 8))
    elif jogada == 6:
        if set == "6":
            set = "o"
            jogador = jogador - 1
            empate = empate + 1
            print(jogada)
        else:
            jogada = (random.randint(0, 8))
    elif jogada == 7:
        if oit == "7":
            oit = "o"
            jogador = jogador - 1
            empate = empate + 1
            print(jogada)
        else:
            jogada = (random.randint(0, 8))
    elif jogada == 8:
        if non == "8":
            non = "o"
            jogador = jogador - 1
            empate = empate + 1
            print(jogada)
        else:
            jogada = (random.randint(0, 8))


def limpar_jogo():
    global pri, seg, ter, qua, qui, sex, set, oit, non
    global empate
    pri = "0"
    seg = "1"
    ter = "2"
    qua = "3"
    qui = "4"
    sex = "5"
    set = "6"
    oit = "7"
    non = "8"
    empate = 0


while comando != "4":

    limpar_jogo()

    if comando == "0":
        menu()

    if comando == "1":
        print("\n---------------INÍCIO DO JOGO---------------\n")
        while empate < 9:

            chama_jogo()

            onde_jogar()

            verifica_vitoria()


        verifica_empate()
        comando = "0"
        menu()

    if comando == "2":
        jogador == 1
        chama_jogo()
        while empate < 9:
            while jogador == 1:

                onde_jogar()
                chama_jogo()

            while jogador == 2:
                contra_bot()
                chama_jogo()

            verifica_vitoria()

        verifica_empate()
        comando = "0"
        menu()



    if comando == "3":
        como_jogar()



contra_bot()