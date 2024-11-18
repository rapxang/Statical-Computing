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


import matplotlib.pyplot as plt

# Plot Column1 vs Column2
plt.scatter(df['Time Spent'], df['Cyber Bullying'], label='Time Spent', color='blue')
plt.scatter(df['Password Security'], df['Cyber Bullying'], label='Password Security', color='Brown')
plt.scatter(df['Enable Security'], df['Cyber Bullying'], label='Enable Security', color='Green')
plt.scatter(df['Sharing Location'], df['Cyber Bullying'], label='CSharing Location', color='Black')
plt.scatter(df['Accept Unknown'], df['Cyber Bullying'], label='Accept Unknown', color='Pink')
plt.scatter(df['Number of Friends'], df['Cyber Bullying'], label='Number of Friends', color='Orange')
plt.scatter(df['Number of Groups'], df['Cyber Bullying'], label='Number of Groups', color='Purple')
plt.scatter(df['Click on Unknown Link'], df['Cyber Bullying'], label='Click on Unknown Link', color='Red')



# Add labels and title
plt.xlabel('Behaviors')
plt.ylabel('Cyber Bullying')
plt.title('Scatter plot of Correlation between Cyber Bullying and Behaviors')
# Show legend
plt.legend(loc = 'lower right')
plt.grid(True)

# Display the plot
plt.show()


import numpy as np
import seaborn as sns

newdf = df [['Cyber Bullying', 'Time Spent', 'Password Security',
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