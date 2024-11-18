from xmlrpc.client import boolean

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('heart.csv')

print('the data is ',type(df))
correlation_matrix = df.corr().round(2)
print(correlation_matrix)
plt.figure(figsize=(10,8))
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, vmax=1 , vmin=-1)
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, vmax=1 , vmin=-1, mask=mask)
plt.title('Pearson Correlation Matrix')
# sns.scatterplot(correlation_matrix)

plt.savefig('heatmap.png')
matrix = correlation_matrix.unstack()
matrix = correlation_matrix[abs(correlation_matrix) >=0.7]

print("Correlation with strong correlation",matrix)

plt.show()




import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([5,6,7,8,9])
def Pearsons_corr(x,y):
    if len(x) == len(y):
        sum_xy = sum((x - x.mean()) * (y-y.mean()))
        sum_x_squarred = sum((x-x.mena())**2)
        sum_Y_squarred = sum((y-y.mean())**2)
        corr = sum_xy/np.np.sqrt(sum_x_squarred*sum_Y_squarred)
    return  corr
print(Pearsons_corr(x,y))
print(Pearsons_corr(x,x))