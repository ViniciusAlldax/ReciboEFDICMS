import numpy as np
import pandas as pd

# Importação do arquivo csv
df = pd.read_csv("T:\DEPARTAMENTOS\AUTOMAÇÃO\Vinícius F\Estudo\heart.csv")

# Transformação do nome das colunas para minuscúlas
colunas = df.columns
colunas_novas = []

for row in colunas:
    var1 = row.lower()
    colunas_novas.append(var1)

df.columns = colunas_novas

# Verificação da quantidade de valores por categoria
# print(df['sex'].value_counts())

colunas_categoricas = ['sex', 'chestpaintype', 'fastingbs', 'restingecg',
                       'exerciseangina', 'st_slope', 'heartdisease']

for row in colunas_categoricas:
    print(f"Contagem de valores da coluna {row}:")
    print(df[row].value_counts())

# Colunas = ['age' (inteiros), 'sex' (binários), 'chestpaintype (quatro tipos)'
# , 'restingbp (variado)','cholesterol (variado)', 'fastingbs (binário)','restingecg
# (três tipos)', 'maxhr (variado)', 'exerciseangina (binário)', 'oldpeak (variado)',
# 'st_slope (três tipos)', 'heartdisease (binário)']