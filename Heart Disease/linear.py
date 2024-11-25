threshold = 0.8
highly_correlated = corr_matrix.unstack().sort_values(ascending=False)
highly_correlated_pairs = highly_correlated[(highly_correlated > threshold) & (highly_correlated < 1)]




lowly
threshold_lower = -0.2
threshold_upper = 0.2
low_correlated = corr_matrix.unstack().sort_values(ascending=True)
low_correlated_pairs = low_correlated[(low_correlated < threshold_upper) & (low_correlated > threshold_lower) & (low_correlated != 1)]


cleaned_df = df.dropna(thresh=len(df) * 0.3 , axis=1)

from sklearn.preprocessing import OneHotEncoder
onehot_encoder = OneHotEncoder(sparse=False)
encoded_data = onehot_encoder.fit_transform(df,columns = ['Country'])
print('The encoded Country column are as follows:',encoded_data)


print(cleaned_df.columns)
df.drop_duplicates(subset=['InvoiceNo'], keep='first',inplace=True)