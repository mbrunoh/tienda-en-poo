import pandas as pd

df = pd.read_csv('database.csv')
for row in df.itertuples(index=False):
    print(row.nombre, row.precio, row.stock)