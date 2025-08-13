def exercicio1():
    i = 1
    while i <= 10:
        print(i)
        i += 1

def exercicio2():
    soma = 0
    i = 1
    while i <= 100:
        soma += i
        i += 1
    print("Soma:", soma)

def exercicio3():
    i = 1
    while i <= 10:
        print(f"5 x {i} = {5*i}")
        i += 1

def exercicio4():
    i = 2
    while i <= 20:
        print(i)
        i += 2

def exercicio5():
    i = 1
    while i <= 10:
        print(f"{i} ao quadrado é {i**2}")
        i += 1
def exercicio6():
    i = 10
    while i >= 0:
        print(i)
        i -= 1

def exercicio7():
    i = 1
    resultado = 1
    while i <= 5:
        resultado *= i
        i += 1
    print(resultado)

def exercicio8():
    i = 0
    while i <= 20:
        if i % 2 == 1:
            print(i)
        i += 1
def exercicio9():
    vogais = "aeiouAEIOU"
    contagem_vogais = {}
    i = 0
    texto = input("Digite um texto: ")

    while i < len(texto):
        letra = texto[i]
        if letra in vogais:
            contagem_vogais[letra] = contagem_vogais.get(letra, 0) + 1
        i += 1

    print("Vogais encontradas e suas quantidades:")
    for vogal, quantidade in contagem_vogais.items():
        print(f"{vogal}: {quantidade}")

def exercicio10():
    lista_compras =  []
    
    while True:
        item = str(input("Digite os itens na lista ou digite sair para sair: "))
        if item.lower() == "sair":
            break
        lista_compras.append(item)
    print("\nSua lista de compras:")
    for i, item in enumerate(lista_compras, 1):
         print(f"{i}. {item}")
    

        


        
    



seletor = int(input("Digite O numero do exercicio desejado,\n "
"Exercicio 1 (1)\n"
"Exercicio 2 (2)\n"
"Exercicio 3 (3)\n"
"Exercicio 5 (5)\n"
"Exercicio 6 (6)\n"
"Exercicio 7 (7)\n"
"Exercicio 8 (8)\n"
"Exercicio 9 (9)\n"
"Exercicio 10 (10):\n "))

if seletor == 1:
    exercicio1()
elif seletor == 2:
    exercicio2()
elif seletor == 3:
    exercicio3
elif seletor == 4:
    exercicio4()
elif seletor == 5:
    exercicio5()
elif seletor == 6:
    exercicio6()
elif seletor == 7:
    exercicio7()
elif seletor == 8:
    exercicio8()
elif seletor == 9:
    exercicio9()
elif seletor == 10:
    exercicio10()
