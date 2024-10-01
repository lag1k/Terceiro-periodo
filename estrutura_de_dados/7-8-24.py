import sys #baixar biblioteca sys

#variaveis para serem globais
idades= []
y = 0
media2 = 0
valor_max = 0
valor_min = 0
mi = 0
ma = 0
intervalo = 0

def add(): #funcação para add itens na lista
    x = int(input("Quantas idades? \n=>"))
    
    for i in range(x):#coleda de idades, com prevenção de input errado
        erro = "Tente novamente valor inválido"

        while True: #restart caso preencha errado
            try:
                idade = int(input(f"Qual a idade {i+1}?\n =>"))
                if 0<idade<=150:
                    idades.append(idade)
                    break
                else:
                    ValueError
                    print(f"============== \n{erro}")  
            except ValueError:
                print(f"============== \n{erro} \n==============")
    
    #levar a contagem de idades para global
    global y
    y = x

    #calculo da media
    media1 = sum(idades)
    global media2
    media2 = media1 / x
    
    #valores minimos e maximos
    global valor_max
    global valor_min    
    valor_max = max(idades)
    valor_min = min(idades)
    
    #intervalo
    inter()
    menu()

def inter(): #funcao do intervalo
    global mi
    global ma
    mi = int(input(f"Qual o menor numero do intervalo? \n=>"))
    ma = int(input(f"Qual o MAIOR numero do intervalo? \n=>"))
    global intervalo
    intervalo = len([ num for num in idades if mi <= num <= ma])#code para ler intervalo, foi dificil mas possivel n recomendo fzr isso nem pro meu inimigo

def listas(): #função para printar lista
    print(f"Sua lista possui {y} idades. \nSua lista é:{idades}. \nSua média é {media2}. \nO máximo é {valor_max}. e o minímo é {valor_min}.")
    print(f"Seus intervalos foi de {mi} ate {ma}, tiveram {intervalo} numeros. \n")
    menu()


def sair(): #fechar o code
    sys.exit
    

def menu(): #menu inicial
    print("=============")
    print("Bem-vindo \nO que deseja? \n")
    s = int(input("1.Adicionar \n2.Relatório \n3.Sair \n=>"))
    print("=============")
    if s == 1:
        add()
    elif s == 2:
        listas()
    elif s == 3:
        sair()

menu()                                    