# import pandas as pd
# df=pd.read_csv('StudentPerformance.csv')
# print(df.head())
#print('The third data is:\n',df.loc[2])
#
# # import csv
# #
# # fields = ['Name', 'Age', 'Gender', 'Grade']
# # rows = [
# #         ['Kunga',26,'Male','A+'],
# #         ['Nyima',25,'Male','A+'],
# #         ['Gurung', 24,'Male,A'],
# #         ['Priyanka',25,'Female','A+'],
# #         ['Riya',23,'Female','A']
# #         ]
# # with open('personaldetails.csv', mode='w') as file:
# #     csvwriter = csv.writer(file)
# #     csvwriter.writerow(fields)
# #     csvwriter.writerows(rows)
#
#
#import csv

import pandas as pd
df= pd.read_csv('personaldetails.csv')
print(df.head())
new_data=['Aditya',27,'Male','A']
df._append(new_data)
print(df.head())


