#assign indexes
from ast import Index
#To import our csv file
import pandas as pd
#To create Numpy array
import numpy as np
#To plot the data
import matplotlib.pyplot as plt
#To organize the data
import seaborn as sns
#To split the data into train and test data
from sklearn.model_selection import train_test_split
#To build our Linear Regression Model
from sklearn.linear_model import LinearRegression
#To test the model
from sklearn import metrics

#////////////////////////////////



#Reading/ imprting the csv file
raw_data = pd.read_csv('heart.csv')
#Printing a summary to understand the data
raw_data.info()
#Viualize the data
sns.pairplot(raw_data)
plt.show()
#assiging indexes
Index(['age','sex','trestbps','chol','thalach','exang'],
dtype='object')

#Assign the x-variblaes
x = raw_data[['age','sex','trestbps','chol','thalach','exang']]
#Assignt the y-variable
y = raw_data['target']

#Splitting the data into training and testing data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)

#Create and instant of the model Linear Regression Model
model = LinearRegression()

#Building the Linear Regression model
model.fit(x_train, y_train)

#Examining the model's coefficients
print(model.coef_)

#The intercept of the Regression model
print(model.intercept_)

#Viewing the coefficients is by placing them in a DataFrame:
print(pd.DataFrame(model.coef_, x.columns, columns = ['Coeff']))

#Predecting Y value by using X-values
predictions = model.predict(x_test)

#To compare the predected values of (Y) with the values of (Y-test)
plt.scatter(y_test, predictions)
plt.show()

#Ploting the residuals (The difference between the actual data and the predicted data)
plt.hist(y_test - predictions)
plt.show()

#Calculating the Mean Absolute Error
metrics.mean_absolute_error(y_test, predictions)

#To test the model by calcualting the mean square error
metrics.mean_squared_error(y_test, predictions)

#Calculating the Root Square Error
np.sqrt(metrics.mean_squared_error(y_test, predictions))
