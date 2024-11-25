threshold = 0.8  # You can adjust this threshold based on what you consider "highly correlated"
highly_correlated = corr_matrix.unstack().sort_values(ascending=False)

# Filter out pairs where the correlation is above the threshold but not equal to 1 (to avoid self-correlation)
highly_correlated_pairs = highly_correlated[(highly_correlated > threshold) & (highly_correlated < 1)]




lowly

threshold_lower = -0.2
threshold_upper = 0.2

# Unstack the correlation matrix to get all pairs and their correlation coefficients
low_correlated = corr_matrix.unstack().sort_values(ascending=True)

# Filter pairs where the absolute correlation is low (between -0.2 and 0.2)
low_correlated_pairs = low_correlated[(low_correlated < threshold_upper) & (low_correlated > threshold_lower) & (low_correlated != 1)]