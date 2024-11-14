import pandas as pd
df = pd.read_csv("Fake Profile.csv")
print(df.head())

print('The shape of the dataset is \n',df.shape)
print(df.isna().sum())
print(df.columns)


# Calculate correlation between column ‘A’ and ‘B’
correlation_ts = df['Fake Profile'].corr(df['Time Spent'])
correlation_ps = df['Fake Profile'].corr(df['Password Security'])
correlation_es = df['Fake Profile'].corr(df['Enable Security'])
correlation_sl = df['Fake Profile'].corr(df['Sharing Location'])
correlation_au = df['Fake Profile'].corr(df['Accept Unknown'])
correlation_nof = df['Fake Profile'].corr(df['Number of Friends'])
correlation_nog = df['Fake Profile'].corr(df['Number of Groups'])
correlation_coul = df['Fake Profile'].corr(df['Click on Unknown Link'])

print("\nThe correlation between Fake Profile and Time Spent is",correlation_ts)
print("\nThe correlation between Fake Profile and Password Security is",correlation_ps)
print("\nThe correlation between Fake Profile and Enable Security is",correlation_es)
print("\nThe correlation between Fake Profile and Sharing Location is",correlation_sl)
print("\nThe correlation between Fake Profile and Accept Unknown is",correlation_au)
print("\nThe correlation between Fake Profile and Number of Friends is",correlation_nof)
print("\nThe correlation between Fake Profile and Number of Groups is",correlation_nog)
print("\nThe correlation between Fake Profile and Click on Unknown Link is",correlation_coul)




import matplotlib.pyplot as plt

# Plot Column1 vs Column2
plt.scatter(df['Time Spent'], df['Fake Profile'], label='Time Spent', color='blue')
plt.scatter(df['Password Security'], df['Fake Profile'], label='Password Security', color='red')
plt.scatter(df['Enable Security'], df['Fake Profile'], label='Enable Security', color='Green')
plt.scatter(df['Sharing Location'], df['Fake Profile'], label='CSharing Location', color='Black')
plt.scatter(df['Accept Unknown'], df['Fake Profile'], label='Accept Unknown', color='Pink')
plt.scatter(df['Number of Friends'], df['Fake Profile'], label='Number of Friends', color='Orange')
plt.scatter(df['Number of Groups'], df['Fake Profile'], label='Number of Groups', color='Purple')
plt.scatter(df['Click on Unknown Link'], df['Fake Profile'], label='Click on Unknown Link', color='Brown')



# Add labels and title
plt.xlabel('Behaviors')
plt.ylabel('Fake Profile')
plt.title('Scatter plot of Correlation between Fake Profile and Behaviors')
# Show legend
plt.legend(loc = 'lower right')
plt.grid(True)

# Display the plot
plt.show()