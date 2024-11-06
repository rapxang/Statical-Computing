# Reading the dataset using pandas Dataframe
import pandas as pd
df = pd.read_csv('online_sales_dataset.csv')
# printing the first five data in the Dataframe
print(df.head())

# Determining the shape of the Dataframe(i.e. number of rows and columns
print('The number of rows and columns of the dataframe are as follows:\n',df.shape)
# The Dataframe has  49782 rows and 17 columns

# Examining the Dataframe for the missing values
print('\nThe number of missing values in the respective columns are as follows:\n')
print(df.isna().sum())

# determining the duplicate values in the cleaned dataframe
df.drop_duplicates(subset=['InvoiceNo'], keep='first',inplace=True)

# Dropping the rows that have missing values since the Dataframe is large size dropping the rows that
# has null value doesnt affect the study as a whole
cleaned_df = df.dropna()
print(cleaned_df.shape)
print(cleaned_df.isna().sum())
# after dropping the missing rows, the cleaned dataframe is brought down to 44804 rows and 17 columns
