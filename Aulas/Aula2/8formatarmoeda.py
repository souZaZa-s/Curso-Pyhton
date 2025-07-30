import locale

locale.setlocale(locale.LC_ALL, "pt_br.UTF-8")

salario = 9999.99

salario_formatado = locale.currency(salario, grouping = True)
print(salario)
print(salario_formatado)