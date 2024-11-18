from operator import index
from unittest.mock import inplace

import pandas as pd
# Read the CSV file
df = pd.read_csv('data.csv')
# Display the first 5 rows
print(df.head())


# Filter the DataFrame
filtered_df = df[df['total_profit'] > 100000]
# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv('filtered_data.csv', index=False)


# Add a new column
df['Total Units Sold'] = df['total_units'] / 0.8
# Save the modified DataFrame to a new CSV file
df.to_csv('modified_data.csv', index=False)


# Rename the column
df.rename(columns={'total_profit': 'Profit'}, inplace=True)
# Save the updated DataFrame to a new CSV file
df.to_csv('renamed_data.csv', index=False)


# Sort the DataFrame by Salary in descending order
sorted_df = df.sort_values(by='total_units', ascending=False)
# Save the sorted DataFrame to a new CSV file
sorted_df.to_csv('sorted_data.csv', index=False)



dff=pd.read_csv('modified_data.csv')
print(dff.head())

# Select specific columns
subset_dff = dff[['total_profit', 'Total Units Sold']]
# Save the subset to a new CSV file
subset_dff.to_csv('subset_data.csv', index=False)

















