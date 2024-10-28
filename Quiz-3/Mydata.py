import csv
fields = ['Tutoring_Sessions','Family_Income','Teacher_Quality','School_Type']
rows =  [
    [0,'Low','Medium','Public'],
    [2, 'Low', 'Medium', 'Public'],
    [2, 'Low', 'Medium', 'Public']
]
with open('MYdata.csv', mode='w') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

