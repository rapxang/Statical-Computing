import pandas as pd
import csv
with open('titanic.csv',mode='r')as file:
    csvdata=csv.reader(file)

    for lines in csvdata:
        print(lines)