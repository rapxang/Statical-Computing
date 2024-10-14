# import pandas as pd
import csv
# with open('files.csv',mode='r')as file:
#     csvdata=csv.reader(file)
#
#     for lines in csvdata:
#         print(lines)

fields=['Name','Age','Grade']
rows=[
    ['Kunga',25,'A'],
    ['Nyima',24,'A+'],
    ['Gurung',22,'A']
    ]
filename="Details.csv"
with open (filename,'w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
