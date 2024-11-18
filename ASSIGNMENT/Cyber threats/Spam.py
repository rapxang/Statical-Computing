import pandas as pd
df = pd.read_csv("Spam.csv")
print(df.head())

print('The shape of the dataset is \n',df.shape)
print(df.isna().sum())
print(df.columns)


# Calculate correlation between column ‘A’ and ‘B’
correlation_ts = df['Spam'].corr(df['Time Spent'])
correlation_ps = df['Spam'].corr(df['Password Security'])
correlation_es = df['Spam'].corr(df['Enable Security'])
correlation_sl = df['Spam'].corr(df['Sharing Location'])
correlation_au = df['Spam'].corr(df['Accept Unknown'])
correlation_nof = df['Spam'].corr(df['Number of Friends'])
correlation_nog = df['Spam'].corr(df['Number of Groups'])
correlation_coul = df['Spam'].corr(df['Click on Unknown Link'])

print("\nThe correlation between Spam and Time Spent is",correlation_ts)
print("\nThe correlation between Spam and Password Security is",correlation_ps)
print("\nThe correlation between Spam and Enable Security is",correlation_es)
print("\nThe correlation between Spam and Sharing Location is",correlation_sl)
print("\nThe correlation between Spam and Accept Unknown is",correlation_au)
print("\nThe correlation between Spam and Number of Friends is",correlation_nof)
print("\nThe correlation between Spam and Number of Groups is",correlation_nog)
print("\nThe correlation between Spam and Click on Unknown Link is",correlation_coul)




import matplotlib.pyplot as plt


plt.scatter(df['Password Security'], df['Spam'], label='Password Security', color='red')
plt.scatter(df['Enable Security'], df['Spam'], label='Enable Security', color='Brown')
plt.scatter(df['Sharing Location'], df['Spam'], label='CSharing Location', color='Black')
plt.scatter(df['Accept Unknown'], df['Spam'], label='Accept Unknown', color='Pink')
plt.scatter(df['Number of Friends'], df['Spam'], label='Number of Friends', color='Orange')
plt.scatter(df['Number of Groups'], df['Spam'], label='Number of Groups', color='Purple')
plt.scatter(df['Click on Unknown Link'], df['Spam'], label='Click on Unknown Link', color='Green')



# Add labels and title
plt.xlabel('Behaviors')
plt.ylabel('Spam')
plt.title('Scatter plot of Correlation between Spam and Behaviors')
# Show legend
plt.legend(loc = 'lower right')
plt.grid(True)

# Display the plot
plt.show()






