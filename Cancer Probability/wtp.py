import csv

data=[['Welcome'],[2],['Python']]
file=open('officedata.csv','w+',newline='')
with file:
     write=csv.writer(file)
     write.writerows(data)
