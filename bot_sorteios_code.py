import time, random, re
import pyautogui
from datetime import date
from datetime import datetime
import pdb

# Envia o emoji que deve estar na area de transferencia
def emoji():

    pyautogui.hotkey("ctrl", "v")


def night_check():
    now = str(datetime.now())

    horario = now.split()[1].split(":")

    if int(horario[0]) >= 1 and int(horario[0]) <= 2:
        time.sleep(5 * 3600)


# função resposnavel por adiconar mais aleatoriedade ao codigo
def choose():
    escolhe = random.randint(1, 3)
    if escolhe == 3:
        emoji()
    elif escolhe == 2:
        time.sleep(random.uniform(5, 10))


def bot_mode(modo, i):

    if modo == 1:
        if i > 15:
            time.sleep(random.uniform(i - 5, i + 20))
        elif i > 50:
            time.sleep(random.uniform(i - 15, i + 20))
        else:
            time.sleep(random.uniform(10, 18))

    elif modo == 2:
        if i > 15:
            time.sleep(random.uniform(i - 10, i + 10))
        elif i > 50:
            time.sleep(random.uniform(i - 30, i + 5))
        else:
            time.sleep(random.uniform(5, 15))

    elif modo == 3:
        if i > 15:
            time.sleep(random.uniform(i - 20, i + 0))
        elif i > 50:
            time.sleep(random.uniform(i - 30, i - 5))
        else:
            time.sleep(random.uniform(5, 10))

    else:
        print("INVALID INPUT\nO modo default (2. Moderado) foi acionado")
        modo = 2
        bot_mode(modo, i)

    if i == 200:
        time.sleep(random.uniform(3000, 3500))


# função com o papel de criar o cabeçalho (---- dia ----), alem disso,
# ela é responsavel por checar se o dia que esta no cabeçalho é o de hj
def handling_file():

    # abre o log.txt
    f = None
    try:
        f = open("log.txt", "r")
    except:
        print("Não foi possivel abrir o arquivo log.txt")

    # roda o file contando quais linhas são cabeçalho (---- dia ----)
    _ = contador = 0
    for line in f:
        line = line.rstrip()
        if len(line) > 0 and line[0] == "-":
            _ += 1

    # abre novamente o file
    try:
        f = open("log.txt", "r")
    except:
        print("Não foi possivel abrir o arquivo log.txt")

    # roda o file contando novamente contando os cabeçalhos
    for Line in f:
        Line = Line.rstrip()
        if len(Line) > 0 and Line[0] == "-":
            contador += 1
        # barra ate a ultima linha, a do dia mais atual
        if contador != _:
            continue
        nums = re.findall("[0-9]+", Line)

        # compara a data que ta no cabeçalho com a data de hoje
        f = open("log.txt", "a+")
        if int(date.today().day) == int(nums[0]):
            break
        else:
            f.write(
                f"\n----------- {time.strftime('%d-%m-%Y', time.localtime())} -------------\n."
            )
            break
    f.close()


# função responsavel por adicionar de forma formatada e eficiente o numero de
# iterações e o horario, ao documento log.txt
def file_writing(i):

    # abre o arquivo
    try:
        fh = open("log.txt", "r")
    except:
        print("Não foi possivel abrir o arquivo log.txt")

    # usa list comprehension para achar o index da ultima linha do file
    lastline_num = sum(1 for _ in fh)

    # abre novamente o arquivo
    try:
        fh = open("log.txt", "r")
    except:
        print("Não foi possivel abrir o arquivo log.txt")

    # monta uma lista com todas as linhas do arquivo ate o momento
    lines = fh.readlines()

    # abre novamente o arquivo
    try:
        fh = open("log.txt", "r")
    except:
        print("Não foi possivel abrir o arquivo log.txt")

    # inicia algumas variaveis com valor nulo
    lastline_str = ""
    contador = sinal = 0
    data = []
    # roda o arquivo iterando o contador
    for line in fh:
        line = line.rstrip()
        contador += 1
        # condição de que line seja a ultima linha do arquivo
        if contador == lastline_num:
            lastline_str = line
            # cria uma lista com os elementos da ultima linha
            data = line.split()

    # verifica se a ultima linha é o cabeçalho ou o num de iterações
    if i != 1 or lastline_str == ".":
        # manda um sinal pra truncar o .
        if lastline_str == ".":
            sinal = True
        # abre o arquivo truncando ele antes
        try:
            fh = open("log.txt", "w")
        except:
            print("Não foi possivel abrir o arquivo log.txt")
        # reescreve todas as linhas, menos a ultima
        for Line in lines:
            if Line.strip("\n") != lastline_str:
                fh.write(Line)

    # abre o arquivo porem mantendo o inicio na ultima linha do file
    try:
        fh = open("log.txt", "a")
    except:
        print("Não foi possivel abrir o arquivo log.txt")

    # formata o i menor que 10 com o 0 antes
    j = i
    i = str(i)
    if j < 10:
        i = "0" + i

    # reescreve a linha com o atual valor a iteração adicionando o 1 horario
    # quando o sinal é falso precisa pular a linha
    if i == "01" and sinal == False:
        fh.write(
            f'\n{i}                           {time.strftime("%H:%M:%S", time.localtime())}'
        )
    # quado o sinal é vdd a linha ja é uma em branco
    elif i == "01" and sinal == True:
        fh.write(
            f'{i}                           {time.strftime("%H:%M:%S", time.localtime())}'
        )
    # reescreve a linha com o atual valor a iteração matendo o horario anterior
    else:
        fh.write(f"{i}                           {data[1]}")


# tupla com as palavras que serão comentadas
palavras = (
    u"EU QUERO",
    u"EU QUEROO",
    u"Eu Queroo",
    u"Eu Quero",
    u"Eu querooo",
    u"Eu queroo",
    u"Eu quero",
    u"eu querooo",
    u"eu queroo",
    u"eu quero",
)

print("\nWorking...")

# cabeçalho perguntando a intensidade que o bot comentara
modo = None
print("\n\nEscolha o modo de operação do bot:")
print("1. Leve     [cerca de coments/min]")
print("2. Moderado [cerca de coments/min]")
print("3. Intenso  [cerca de coments/min]")
while modo == None:
    try:
        modo = int(input("Digite o numero do modo escolhido: "))
    except ValueError:
        pass
print("\n")

i = 1
# Looping principal
while True:
    time.sleep(6)

    word = random.choice(palavras)
    pyautogui.click()
    try:
        pyautogui.typewrite(word)
    except:
        print("\n\tNÃO FOI POSSIVEL COMENTAR")

    if word == " " or word == "":
        emoji()

    bot_mode(modo, i)
    night_check()
    pyautogui.press("enter")
    print("Numero de comentarios feitos:", i)

    handling_file()
    file_writing(i)

    i += 1
