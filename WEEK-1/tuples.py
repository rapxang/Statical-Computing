#1-Write a Python program to create a tuple.
tuples = (1, 2, 3, 4, 5)
print(tuples)

#2-Write a Python program to create a tuple with different data types
information = ("Kunga", 25, "Erie", 9297278830, 5.5)
#3-Write a Python program to unpack a tuple into several variables.
name, age, address, phone, height = information
print(name)
print(address)
print(age)
print(height)

import pandas as pd

pd.read_csv("Employee Sample Data.csv")
