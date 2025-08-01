def calcularMedia():
    print("Bem Vindo ao calculador de medias;)")
    nt1 = int(input("Digite a nota da primeira prova: "))
    nt2 = int(input("Digite a nota da segunda prova: "))
    nt3 = int(input("Digite a nota da terceira prova: "))
    media = (nt1 + nt2 + nt3) / 3
    if media == 10:
        print(f"Sua média foi 10, Parabens!!")
    elif media >= 7:
        print(f"Sua média foi: {round(media, 2)}, muito bom!")
    elif media >= 5:
        print(f"Sua media foi: {round(media, 2)}, boa recuperação")
    else:
        print(f"Sua media foi: {round(media, 2)}, REPROVADO")

    
calcularMedia()