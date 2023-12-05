import openpyxl

# Criar uma planilha (salvar na variável book)
book = openpyxl.Workbook()

# Como visualizar páginas existentes
print(book.sheetnames)

# Criar uma página
book.create_sheet('Frutas')

# Como selecionar uma página
frutas_page = book['Frutas']

# Como criar colunas e linhas
frutas_page.append(['Fruta', ' Quantidade', 'Preço'])
frutas_page.append(['Banana', ' 9', '0,99'])
frutas_page.append(['Maça', ' 7', '9,00'])
frutas_page.append(['Pera', ' 11', '1,00'])
frutas_page.append(['Uva', '3', '0,50'])

# Salvar a planilha
book.save('Planilha de Compras.xlsx')

