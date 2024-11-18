import pandas as pd
import seaborn as sns
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





import matplotlib.pyplot as plt
# Plot Column1 vs Column2
plt.scatter(df['Time Spent'], df['Clickjacking'], label='Time Spent', color='blue')

# Plot Column1 vs Column3
plt.scatter(df['Password Security'], df['Clickjacking'], label='Password Security', color='red')
plt.scatter(df['Enable Security'], df['Clickjacking'], label='Enable Security', color='Green')
plt.scatter(df['Sharing Location'], df['Clickjacking'], label='CSharing Location', color='Black')
plt.scatter(df['Accept Unknown'], df['Clickjacking'], label='Accept Unknown', color='Pink')
plt.scatter(df['Number of Friends'], df['Clickjacking'], label='Number of Friends', color='Orange')
plt.scatter(df['Number of Groups'], df['Clickjacking'], label='Number of Groups', color='Purple')
plt.scatter(df['Click on Unknown Link'], df['Clickjacking'], label='Click on Unknown Link', color='Brown')



# Add labels and title
plt.xlabel('Behaviors')
plt.ylabel('Clickjacking')
plt.title('Scatter plot of Correlation between Clickjacking and Behaviors')

# Show legend
plt.legend(loc = 'lower right')
plt.grid(True)

# Display the plot
plt.show()



newdf = df [['Clickjacking', 'Time Spent', 'Password Security',
       'Enable Security', 'Sharing Location', 'Accept Unknown',
       'Number of Friends', 'Number of Groups', 'Click on Unknown Link']]


correlation_matrix = newdf.corr().round(2)

print(correlation_matrix)
plt.figure(figsize=(10,8))
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, vmax=1 , vmin=-1)
plt.title('Pearson Correlation Matrix')
# sns.scatterplot(correlation_matrix)
plt.show()

