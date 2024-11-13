import pandas as pd
import numpy as np

df = pd.read_csv("Clickjacking.csv")
print(df.head())

print('The shape of the dataset is \n',df.shape)
print(df.isna().sum())
print(df.columns)


# Calculate correlation between column ‘A’ and ‘B’
correlation_ts = df['Clickjacking'].corr(df['Time Spent'])
correlation_ps = df['Clickjacking'].corr(df['Password Security'])
correlation_es = df['Clickjacking'].corr(df['Enable Security'])
correlation_sl = df['Clickjacking'].corr(df['Sharing Location'])
correlation_au = df['Clickjacking'].corr(df['Accept Unknown'])
correlation_nof = df['Clickjacking'].corr(df['Number of Friends'])
correlation_nog = df['Clickjacking'].corr(df['Number of Groups'])
correlation_coul = df['Clickjacking'].corr(df['Click on Unknown Link'])

print("\nThe correlation between Clickjacking and Time Spent is",correlation_ts)
print("\nThe correlation between Clickjacking and Password Security is",correlation_ps)
print("\nThe correlation between Clickjacking and Enable Security is",correlation_es)
print("\nThe correlation between Clickjacking and Sharing Location is",correlation_sl)
print("\nThe correlation between Clickjacking and Accept Unknown is",correlation_au)
print("\nThe correlation between Clickjacking and Number of Friends is",correlation_nof)
print("\nThe correlation between Clickjacking and Number of Groups is",correlation_nog)
print("\nThe correlation between Clickjacking and Click on Unknown Link is",correlation_coul)








