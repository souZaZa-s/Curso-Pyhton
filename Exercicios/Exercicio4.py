def frequenciaOuvalor():
    print("Bem vindo ao calculador de desconto:")
    semitotal = float(input("Por Favor, insira o valor total dos produtos: "))
    frequencia = str(input("Você é cliente frequente?, (sim) ou (nao): "))
    
    if semitotal >= 1000 or frequencia == "sim":
        print("Voce tem desconto:)")
    else: 
        print("Voce não tem desconto:(")

def oddoreven():
    num = int(input("Bem vindo ao verificador de par ou impar digite seu numero: "))
    if (num == 0):
        print("Seu numero é Zero!")
    elif(num % 2 == 0):
        print("Seu numero é Par!")
    else:
        print("Seu numero é Impar!")

def posOrneg():
    num = int(input("Bem vindo ao verificador de polaridade digite seu numero: "))
    if num > 0:
        print("Seu numero é positivo!")
    elif num == 0:
        print("Seu numero é Zero!")
    elif num < 0:
        print("Seu numero é Negativo!")

posOrneg()