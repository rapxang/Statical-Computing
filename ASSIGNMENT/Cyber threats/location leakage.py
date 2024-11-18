import pandas as pd
df = pd.read_csv("location leakage.csv")
print(df.head())

print('The shape of the dataset is \n',df.shape)
print(df.isna().sum())
print(df.columns)


# Calculate correlation between column ‘A’ and ‘B’
correlation_ts = df['Location Leakage'].corr(df['Time Spent'])
correlation_ps = df['Location Leakage'].corr(df['Password Security'])
correlation_es = df['Location Leakage'].corr(df['Enable Security'])
correlation_sl = df['Location Leakage'].corr(df['Sharing Location'])
correlation_au = df['Location Leakage'].corr(df['Accept Unknown'])
correlation_nof = df['Location Leakage'].corr(df['Number of Friends'])
correlation_nog = df['Location Leakage'].corr(df['Number of Groups'])
correlation_coul = df['Location Leakage'].corr(df['Click on Unknown Link'])

print("\nThe correlation between Location Leakage and Time Spent is",correlation_ts)
print("\nThe correlation between Location Leakage and Password Security is",correlation_ps)
print("\nThe correlation between Location Leakage and Enable Security is",correlation_es)
print("\nThe correlation between Location Leakage and Sharing Location is",correlation_sl)
print("\nThe correlation between Location Leakage and Accept Unknown is",correlation_au)
print("\nThe correlation between Location Leakage and Number of Friends is",correlation_nof)
print("\nThe correlation between Location Leakage and Number of Groups is",correlation_nog)
print("\nThe correlation between Location Leakage and Click on Unknown Link is",correlation_coul)

import matplotlib.pyplot as plt

# Plot Column1 vs Column2
plt.scatter(df['Time Spent'], df['Location Leakage'], label='Time Spent', color='blue')
plt.scatter(df['Password Security'], df['Location Leakage'], label='Password Security', color='red')
plt.scatter(df['Enable Security'], df['Location Leakage'], label='Enable Security', color='Green')
plt.scatter(df['Sharing Location'], df['Location Leakage'], label='CSharing Location', color='Black')
plt.scatter(df['Accept Unknown'], df['Location Leakage'], label='Accept Unknown', color='Pink')
plt.scatter(df['Number of Friends'], df['Location Leakage'], label='Number of Friends', color='Brown')
plt.scatter(df['Number of Groups'], df['Location Leakage'], label='Number of Groups', color='Purple')
plt.scatter(df['Click on Unknown Link'], df['Location Leakage'], label='Click on Unknown Link', color='Orange')



# Add labels and title
plt.xlabel('Behaviors')
plt.ylabel('Location Leakage')
plt.title('Scatter plot of Correlation between Location Leakage and Behaviors')
# Show legend
plt.legend(loc = 'lower right')
plt.grid(True)

# Display the plot
plt.show()





import numpy as np
import seaborn as sns

newdf = df [['Location Leakage', 'Time Spent', 'Password Security',
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