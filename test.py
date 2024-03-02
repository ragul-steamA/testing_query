import pandas as pd

df = pd.read_excel('wallet_data.xlsx', usecols='A,B')

print(df)

for i in df.index:
    print( df['phone'][i])
    print(df['wallet_balance'][i])
