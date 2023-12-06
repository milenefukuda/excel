import openpyxl

# Carregando o arquivo
book = openpyxl.load_workbook('Planilha de Compras.xlsx')

# Selecionando uma página
frutas_page = book['Frutas']

# Alterando informações dentro da céular
for rows in frutas_page.iter_rows(min_row=1,max_row=5):
    for cell in rows:
        if cell.value == 'Uva':
            cell.value = 'Fruta 1'

# Salvar as alterações
book.save('Planilha de Compras v2.xlsx')