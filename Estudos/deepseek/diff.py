import pandas as pd

# Use read_csv para arquivos .csv
df1 = pd.read_csv('539.csv')
df2 = pd.read_csv('540.csv')


print(df1.columns)
print(df2.columns)

exit

diferencas = df1.compare(df2)
print(diferencas)
