import pandas as pd
df = pd.read_csv("Cyber bullying.csv")
print(df.head())

print('The shape of the dataset is \n',df.shape)
print(df.isna().sum())
print(df.columns)


# Calculate correlation between column ‘A’ and ‘B’
correlation_ts = df['Cyber Bullying'].corr(df['Time Spent'])
correlation_ps = df['Cyber Bullying'].corr(df['Password Security'])
correlation_es = df['Cyber Bullying'].corr(df['Enable Security'])
correlation_sl = df['Cyber Bullying'].corr(df['Sharing Location'])
correlation_au = df['Cyber Bullying'].corr(df['Accept Unknown'])
correlation_nof = df['Cyber Bullying'].corr(df['Number of Friends'])
correlation_nog = df['Cyber Bullying'].corr(df['Number of Groups'])
correlation_coul = df['Cyber Bullying'].corr(df['Click on Unknown Link'])

print("\nThe correlation between Cyber Bullying and Time Spent is",correlation_ts)
print("\nThe correlation between Cyber Bullying and Password Security is",correlation_ps)
print("\nThe correlation between Cyber Bullying and Enable Security is",correlation_es)
print("\nThe correlation between Cyber Bullying and Sharing Location is",correlation_sl)
print("\nThe correlation between Cyber Bullying and Accept Unknown is",correlation_au)
print("\nThe correlation between Cyber Bullying and Number of Friends is",correlation_nof)
print("\nThe correlation between Cyber Bullying and Number of Groups is",correlation_nog)
print("\nThe correlation between Cyber Bullying and Click on Unknown Link is",correlation_coul)






