import pandas as pd
import csv
with open('data.csv',mode='r')as file:
    csvdata=csv.reader(file)

    for lines in csvdata:
        print(lines)
# titanic_data=pd.read_csv('titanic.csv')
# print(titanic_data.head(5))
# print(titanic_data.describe())
