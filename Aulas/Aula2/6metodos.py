nomecompleto = input("digite seu nome completo: ")
 
print(f"1- quantidade de caracteres: {len(nomecompleto)}")
 
print(f'2 - nome em maiusculo: {nomecompleto.upper()}')
 
print(f'3 - nome em minusculo: {nomecompleto.lower()}')
 
print(f'4 - nome sem espaço: {nomecompleto.replace(' ', '')}')
 
print(f'5 - tem somente letras? (temos que tirar os espaços) {nomecompleto.replace(' ', '').isalpha()}')
 
print(f'6 - é alfanumerico? (temos que tirar os espaços) {nomecompleto.replace(' ', '').isalnum()}')
 