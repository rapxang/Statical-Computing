import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('cancer-probabilities.csv')
print(df.head(10))
# print(df.Display.option.max_rows())
print(df.isna().sum())