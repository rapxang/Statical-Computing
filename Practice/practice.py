import pandas as pd
# Load the CSV file into a DataFrame
employee_data = pd.read_csv('information.csv')
# Check the structure of the DataFrame
print("Column Names:")
print(employee_data.columns)
print("\nData Types:")
print(employee_data.dtypes)
print("\nSummary Statistics:")
print(employee_data.describe())
# Handle missing values
employee_data.dropna(subset=['salary'], inplace=True)
# Remove duplicates
employee_data.drop_duplicates(subset=['employee_id'], keep='first',inplace=True)
# Convert date column to datetime objects
employee_data['hire_date'] = pd.to_datetime(employee_data['hire_date'])
# Calculate the average salary
average_salary = employee_data['salary'].mean()
# Identify the highest and lowest-paid employees
highest_paid = employee_data[employee_data['salary'] ==
employee_data['salary'].max()]
lowest_paid = employee_data[employee_data['salary'] ==
employee_data['salary'].min()]
# Find out how many employees were hired each year
employee_data['hire_year'] = employee_data['hire_date'].dt.year
hiring_per_year = employee_data['hire_year'].value_counts()




# Calculate the average salary
average_salary = employee_data['salary'].mean()
# Identify the highest and lowest-paid employees
highest_paid = employee_data[employee_data['salary'] ==
employee_data['salary'].max()]
lowest_paid = employee_data[employee_data['salary'] ==
employee_data['salary'].min()]
# Find out how many employees were hired each year
employee_data['hire_year'] = employee_data['hire_date'].dt.year
hiring_per_year = employee_data['hire_year'].value_counts()



# Determine the average salary and performance rating for each department
department_stats = employee_data.groupby('department').agg({'salary':
'mean', 'performance_rating': 'mean'})
# Identify which department has the highest and lowest average salary
highest_avg_salary_dept = department_stats[department_stats['salary'] ==
department_stats['salary'].max()]
lowest_avg_salary_dept = department_stats[department_stats['salary'] ==
department_stats['salary'].min()]


# Calculate the average tenure (years of service) for employees
current_year = pd.Timestamp.now().year
employee_data['years_of_service'] = current_year - employee_data['hire_year']
average_tenure = employee_data['years_of_service'].mean()
# Identify employees with the longest and shortest tenures
longest_tenure = employee_data[employee_data['years_of_service'] ==
employee_data['years_of_service'].max()]
shortest_tenure = employee_data[employee_data['years_of_service'] ==
employee_data['years_of_service'].min()]
