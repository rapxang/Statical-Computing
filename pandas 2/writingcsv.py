import csv
fields = ['Name', 'Branch', 'Year', 'CGPA']

rows = [
    ['Nikhil', 'COE','2','9.0'],
    ['Sanchit', 'COE', '2','9.1'],
    ['Aditya','IT','2','9.3'],
    ['Sagar','SE','1','9.5'],
    ['Prateek','MCE','3','7.8'],
    ['Sahil','EP','2','9.1']
        ]
with open('data.csv', 'w') as file:
    #using csv.writer method from csv package
    write = csv.writer(file)

    write.writerow(fields)
    write.writerows(rows)

