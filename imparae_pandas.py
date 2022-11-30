import pandas as pd

from openpyxl.workbook import Workbook

df_excel = pd.read_excel('regions.xlsx')
df_txt = pd.read_csv('Names.csv', header=None)
df_csv = pd.read_csv('data.txt', delimiter='\t')
#Names non ha header=None ed allora glieli assegno di seguito
df_txt.columns=['First', 'Last', 'Address', 'City', 'State', 'AreaCode', 'x']
df_txt.to_csv('Names_modified.csv')
print(df_txt)

