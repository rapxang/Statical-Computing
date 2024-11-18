
from ast import Index
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

raw_data = pd.read_csv('heart.csv')
raw_data.info()
sns.pairplot(raw_data)
plt.show()
Index(['age','sex','trestbps','chol','thalach','exang'],
dtype='object')

x = raw_data[['age','sex','trestbps','chol','thalach','exang']]
y = raw_data['target']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)

model = LinearRegression()

model.fit(x_train, y_train)

print(model.coef_)
print(model.intercept_)
print(pd.DataFrame(model.coef_, x.columns, columns = ['Coeff']))

predictions = model.predict(x_test)

plt.scatter(y_test, predictions)
plt.show()

plt.hist(y_test - predictions)
plt.show()

metrics.mean_absolute_error(y_test, predictions)
metrics.mean_squared_error(y_test, predictions)
np.sqrt(metrics.mean_squared_error(y_test, predictions))
