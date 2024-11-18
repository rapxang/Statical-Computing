from xmlrpc.client import boolean

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('heart.csv')

print('the data is ',type(df))
correlation_matrix = df.corr().round(2)

plt.figure(figsize=(10,8))
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, vmax=1 , vmin=-1)
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, vmax=1 , vmin=-1, mask=mask)
plt.title('Pearson Correlation Matrix')
# sns.scatterplot(correlation_matrix)
plt.show()
