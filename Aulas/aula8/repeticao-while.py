# For de 1 a 10
for contador in range(1, 10 + 1):
    print(contador)
 
# While de 1 a 10
contador = 1
while contador <= 10:
    print(contador)
    contador += 1
 
# Loop para digitar nome ou sair
while True:
    nome = input('Digite seu nome ou S para sair: ')
    if nome.upper() == 'S':
        break
 
# Loop que encerra ao digitar 0
num = 1
while num != 0:
    num = int(input('Digite um valor (0 para sair): '))
print("fim")
 
# Percorrendo cada letra da string
nome = 'diego'
for letra in nome:
    print(letra)
 
# While percorrendo cada letra pelo índice
contador = 0
while contador < len(nome):
    print(contador)
    print(nome[contador])
    contador += 1
 
 
 
 
lista_numeros = []
while True:
    num = int(input('Digite um número: '))
    lista_numeros.append(num)
    for numero in lista_numeros:
        print(f'Contando até {numero}')
        contador = 1
        while contador <= numero:
            print(contador)
            contador += 1
 
 