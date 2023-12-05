import openpyxl

# Carregando o arquivo
book = openpyxl.load_workbook('Planilha de Compras.xlsx')

# Selecionando uma página
frutas_page = book['Frutas']

# Imprimir os dados de cada linha 
for rows in frutas_page.iter_rows(min_row=2,max_row=4):
    for cell in rows:
        print(cell.value)