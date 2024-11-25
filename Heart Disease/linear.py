import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.linear_model import LinearRegression


df = pd.read_csv('Heart_Disease.csv')

print(df.columns)


X = df[['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca', 'thal']]
y= df ['target']



scaler = StandardScaler()
x_scaled = scaler.fit(X)


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train,y_train)

y_predict = model.predict(X_test)


mse  = mean_squared_error(y_test,y_predict)
print(f"mean squarred error :",mse)

r2= r2_score(y_test,y_predict)
print(f"r2 squarred :",r2)


print(df.corr())

print(f"Coefficient of the model : \n")
print(model.coef_)



coeff = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
print(coeff)


import statsmodels.api as sm
modelsss = sm.OLS(y,X).fit()
print(modelsss.summary())