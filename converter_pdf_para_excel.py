import tabula
import pandas as pd
import os

df = tabula.read_pdf('Ficha Financeira.pdf', pages='all')

df.to_excel('Ficha Financeira 9067320.xlsx', index=False)

current_directory = os.getcwd()
print(f"Diretório Atual: {current_directory}")