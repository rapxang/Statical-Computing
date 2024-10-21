import numpy as np
import pandas as pd
df = pd.read_csv('StudentPerformanceFactors.csv')
print(df.head())
print('The Column names in the datset are:\n',df.columns)
print('\nNumber of Rows and Columns in the dataset is :',df.shape)
print('\nChecking the null values in the dataset',df.isna().sum())
print('\nThe dataset description\n',df.describe())