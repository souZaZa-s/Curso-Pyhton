def menu_principal():
    print('Menu principal')
    print('Digite o código do menu:')
    print('1: Opção 1')
    print('2: Opção 2')
    print('3: Opção 3')
 
def main():
    while True:
        menu_principal()
        opcao = input('Escolha uma opção: ')
       
        if opcao == '1':
            print("Você escolheu a Opção 1")
        elif opcao == '2':
            print("Você escolheu a Opção 2")
        elif opcao == '3':
            print("Você escolheu a Opção 3")
        else:
            print("Opção inválida")
 
main()