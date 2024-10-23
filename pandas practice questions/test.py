import csv

from pandas import Flags

fields = ['Name','Age','Gender']
rows = [
    ['Kunga',26,'Male'],
    ['Nyima',25,'Female'],
    ['Gurung',26,'Male']
]
with open('portfolio.csv', mode='w') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

import pandas as pd
df = pd.read_csv('data.csv')
# print(df.head())



filterred_df= df[df['total_profit']>250000]
filterred_df.to_csv('filterreddata.csv', index=False)


df.rename(columns={'total_profit':'TP'},inplace=True)
df.to_csv('renameddata.csv',index=False)

df['TPAT'] = df['TP'] * 0.5
df.to_csv('new data.csv',index=False)

sorted_data=df.sort_values(by='TPAT', ascending=False)
sorted_data.to_csv('sorted data.csv',index=False)


subdata=df[['TP','TPAT']]
subdata.to_csv('subdata.csv',index=False)


with open('data.csv',mode='r') as f:
    filereader = csv.reader(f)

    for lists in filereader:
        print(lists)
