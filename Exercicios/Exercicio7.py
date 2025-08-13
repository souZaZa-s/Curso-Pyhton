def exercicio1():
    for i in range(1, 11):
        print(i)

def exercicio2():
    soma = sum(range(1, 101))
    print("Soma:", soma)

def exercicio3():
    nomes = ["Alice", "Bob", "Carlos"]
    for nome in nomes:
        print(nome)

def exercicio4():
    for i in range(1, 11):
        print(f"5 x {i} = {5 * i}")

def exercicio5():
    for i in range(2, 21, 2):
        print(i)

def exercicio6():
    for i in range(1, 11):
        print(f"{i} ao quadrado é {i ** 2}")

def exercicio7():
    for i in range(10, 0, -1):
        print(i)

def exercicio8():
    resultado = 1
    for i in range(1, 6):
        resultado *= i
    print(resultado)

def exercicio9():
    for i in range(1, 21, 2):
        print(i)

def exercicio10():
    string = "Hello, World!"
    vogais = "aeiouAEIOU"
    total = sum(1 for letra in string if letra in vogais)
    print("Número de vogais:", total)

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
