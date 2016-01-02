import os, csv

#path to the script
currentPath = os.path.dirname(os.path.abspath(\
    "readingPythonCSVExercises.py"))

#make the spreadsheet path
inputCsv = (currentPath + '\spreadsheet.csv')

#open file in read mode
csvFile = open(inputCsv,'rb')

#create reader object
reader = csv.reader(csvFile, delimiter=',')

#print out the data in the file
'''
for row in reader:
    print row
'''


#add data to an array for further manipulation
readerData = []
for row in reader:
    readerData.append(row)

print readerData
